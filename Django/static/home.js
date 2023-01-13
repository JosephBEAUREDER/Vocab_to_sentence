async function sendText() {
     // ON RÉCUPÈRE LES VARIABLES À ENVOYER AU SERVEUR, ici les mots de la textarea "listvoca"
    var inText = document.getElementById('listvoca').value;

    // ON EMBALLE NOTRE VARIABLE DANS UN DICTIONNAIRE
    // ON PEUT ENVOYER AUTANT DE VARIABLES QU'ON VEUT, ICI ON SE CONTENTE D'ENVOYER inText
    var colis = {
        inText: inText
    }
    console.log('Envoi colis:',colis);


// PARAMÈTRES DE LA REQUÊTE
    const requete = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(colis)
    };

// ENVOI ET RÉCUPÉRATION DE LA RÉPONSE

const response = await fetch('/analyze/', requete)
    const data = await response.json();
    console.log(data);

// on écrit les phrases en anglais et en arabe dans leur textarea respectives
    document.getElementById('resp').innerHTML = data.reponse;
    document.getElementById('engrep').innerHTML = data.reponse1;
    element = document.getElementById('engrep');
// et on cache la traduction en anglais
    element.style.visibility = 'hidden';
    
}
// bouton pour montrer la traduction
function showElement() {
    element = document.getElementById('engrep');
    element.style.visibility = 'visible';
}

