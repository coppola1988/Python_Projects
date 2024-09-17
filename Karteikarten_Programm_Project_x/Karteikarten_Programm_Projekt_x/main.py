from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
import logging
import tempfile
import shutil

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# HOMEPAGE


@app.route('/')
def index():
    return render_template('index.html')


# ADDING NEW CARDS


@app.route('/hinzufuegen', methods=['GET','POST'])
def hinzufuegen():
    if request.method == 'POST':
            front = request.form['front']
            back = request.form["back"]

            if not front or not back:
                return redirect(url_for('index'))
            
            try:
                with open("file.json", "r") as file:
                    dictionary = json.load(file)
            except FileNotFoundError:
                dictionary = {}
            
            dictionary[front] = back
            with open("file.json", "w") as file:
                json.dump(dictionary, file)
            
    return render_template('hinzufuegen.html')


# CHECKING ON THE CARDS


@app.route('/karteikartenverwaltung', methods=['GET', 'POST'])
def karteikartenverwaltung():
    try:
        json_files = [f for f in os.listdir("C:\\Users\\danie\\Downloads\\Kennedy-project-main\\Kennedy-project-main\\") if f.endswith('.json')]
        print(json_files)
        card_list = []
        for json_file in json_files:
            try:
                with open(json_file,"r") as file:
                    cards_dict = json.load(file)
                    card_list.append(cards_dict)
            except FileNotFoundError:
                print(f"{json_file} not found")
            except json.JSONDecodeError:
                print(f"Error decoding {json_file}")            
        
    except FileNotFoundError:
        cards_dict = {}
    
    cards_list = [(json_file, key, value) for json_file, (key, value) in enumerate(cards_dict.items())]
    
    if request.method == 'POST':
        new_key = request.form.get('new_key')
        new_value = request.form.get('new_value')
        
        # Check if the new key already existss
        if new_key in cards_dict:
            logger.warning(f"Key '{new_key}' already exists.")
            flash("Key already exists", "warning")
            return redirect(url_for('karteikartenverwaltung'))
        
        # Update the dictionary
        cards_dict[new_key] = new_value
        
        # Create a temporary file for atomic update
        temp_file_path = tempfile.mktemp()
        
        try:
            # Write the updated dictionary to the temporary file
            with open(temp_file_path, "w") as temp_file:
                json.dump(cards_dict, temp_file)
            
            # Replace the original file with the temporary file
            shutil.move(temp_file_path, "file.json")
            
            logger.info(f"Successfully updated card with new key '{new_key}' and value '{new_value}'.")
            flash("Card successfully updated", "success")
            
            # Redirect to show the updated Karteikartenverwaltung page
            return redirect(url_for('karteikartenverwaltung'))
        
        except Exception as e:
            logger.error(f"Error updating file: {str(e)}")
            os.remove(temp_file_path)  # Clean up temporary file if error occurs
            flash("Failed to update card", "danger")
            return redirect(url_for('karteikartenverwaltung'))
    
    return render_template('karteikartenverwaltung.html', cards=cards_list)



# CARD DETAILS AND EDITING


@app.route('/card_detail/<key>', methods=['GET', 'POST'])
def card_detail(key):
    try:
        with open("file.json", "r") as file:
            cards_dict = json.load(file)
    except FileNotFoundError:
        return "File not found", 404
    
    if request.method == 'POST':
        if 'delete' in request.form:
            # Delete the card
            if key in cards_dict:
                del cards_dict[key]
                with open("file.json", "w") as file:
                    json.dump(cards_dict, file)
                logger.info(f"Successfully deleted card with key '{key}'.")
                flash("Card successfully deleted", "success")
                return redirect(url_for('karteikartenverwaltung'))
            else:
                return "Card not found", 404
        
        new_key = request.form.get('new_key')
        new_value = request.form.get('new_value')
        
        # Check if the new key already exists
        if new_key in cards_dict and new_key != key:
            flash("Key already exists", "warning")
            return redirect(url_for('card_detail', key=key))
        
        # Update the dictionary
        if new_key == key:
            cards_dict[key] = new_value
        else:
            cards_dict[new_key] = cards_dict.pop(key)
        
        # Write the updated dictionary back to the file
        with open("file.json", "w") as file:
            json.dump(cards_dict, file)
        
        flash("Card successfully updated", "success")
        return redirect(url_for('karteikartenverwaltung'))
    
    card_details = cards_dict.get(key)
    
    if card_details:
        return render_template('card_detail.html', key=key, details=card_details)
    else:
        return "Card not found", 404
    

# DELETING CARD


@app.route('/delete_card/<key>', methods=['POST'])
def delete_card(key):
    try:
        with open("file.json", "r") as file:
            cards_dict = json.load(file)
    except FileNotFoundError:
        return "File not found", 404
    
    if key in cards_dict:
        del cards_dict[key]
        
        # Write the updated dictionary back to the file
        with open("file.json", "w") as file:
            json.dump(cards_dict, file)
        
        logger.info(f"Successfully deleted card with key '{key}'.")
        #shows information to the user
        flash("Card successfully deleted", "success")
        return redirect(url_for('karteikartenverwaltung'))
    else:
        return "Card not found", 404
    


def sichere_eingabe(eingabe):
    """Erstellt einen sicheren Dateinamen aus der Eingabe."""
    return "".join([c for c in eingabe if c.isalnum() or c == ' ']).rstrip()

# Bearbeitet Daniele 06.09.2024
@app.route('/new_page', methods=['GET','POST'])
def new_page():

    if request.method == 'POST':
        eingabe = request.form.get("stapelname")
        if not eingabe:
            return "Das Feld 'stapel' wurde nicht ausgefüllt", 400

        action = request.form.get("action")
        print(action)
        dictionary1 = {}
        
        if eingabe:
            print(eingabe)
            dateiname = sichere_eingabe(eingabe)
            if not dateiname:
                return "Ungültiger Dateiname", 400

            pfad = os.path.join( f"{eingabe}.json")
            with open(pfad, "w") as file:
                json.dump(dictionary1, file)
            print(f"Datei {eingabe}.json wurde erfolgreich erstellt.") 
    return render_template('new_page.html')
 

if __name__ == '__main__':
    app.run(debug=True)



