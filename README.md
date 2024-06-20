# Generative Text API

This is a FastAPI application that provides a simple API for generating text based on user input. It uses a pre-trained
model for text generation and supports translation between different languages.

## Usage

The api is still under development and may be slow to respond to request. It is free and does not require a header or an
api key

```
https://generatetext.onrender.com/gen_text/
```

### post request

from_lang and error are optional

```json
{
  "text": "Hello World",
  "from_lang": "auto",
  "to_lang": "es",
  "error": null
}
```

### Result

```json
{
  "text": "Hola señor",
  "to_lang": "es",
  "from_lang": "auto",
  "error": null
}
```
