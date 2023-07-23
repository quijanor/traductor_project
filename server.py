"""
Web Translator Server

This module contains a Flask web application for translating text between English and French.
It uses the machinetranslation.translator module to perform the translations.
"""
from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")

@app.route("/englishToFrench")
def to_french():
    """
    Translates English text to French.

    Retrieves the 'textToTranslate' parameter from the request's query string
    and uses the english_to_french function from the machinetranslation.translator
    module to perform the translation. The translated text is then returned as
    the response.
    """
    text_to_translate = request.args.get('textToTranslate')
    translate_to_french = english_to_french(text_to_translate)
    return translate_to_french

@app.route("/frenchToEnglish")
def to_english():
    """
    Translates French text to English.

    Retrieves the 'textToTranslate' parameter from the request's query string
    and uses the french_to_english function from the machinetranslation.translator
    module to perform the translation. The translated text is then returned as
    the response.
    """
    text_to_translate = request.args.get('textToTranslate')
    translate_to_english = french_to_english(text_to_translate)
    return  translate_to_english

@app.route("/")
def render_index_page():
    """
    Renders the index.html template.

    This function is responsible for rendering the HTML template named "index.html"
    and displaying it as the response for the root route ("/").
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
