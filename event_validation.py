import jsonschema
from jsonschema import ValidationError, validate
import json
from Clases import *
schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "numero": {
            "type": "integer"
        },
        "nombre": {
            "type": "string"
        },
        "apellido": {
            "type": "string"
        },
        "dni": {
            "type": "string"
        },
        "tipo": {
            "type": "string"
        },
        "direccion": {
            "type": "object",
            "properties": {
                "calle": {
                    "type": "string"
                },
                "numero": {
                    "type": "string"
                },
                "ciudad": {
                    "type": "string"
                },
                "provincia": {
                    "type": "string"
                },
                "pais": {
                    "type": "string"
                }
            },
            "required": [
                "calle",
                "numero",
                "ciudad",
                "provincia",
                "pais"
            ]
        },
        "transacciones": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "estado": {
                            "type": "string"
                        },
                        "tipo": {
                            "type": "string"
                        },
                        "cuentaNumero": {
                            "type": "integer"
                        },
                        "cupoDiarioRestante": {
                            "type": "integer"
                        },
                        "cantidadExtraccionesHechas": {
                            "type": "integer"
                        },
                        "monto": {
                            "type": "integer"
                        },
                        "fecha": {
                            "type": "string"
                        },
                        "numero": {
                            "type": "integer"
                        },
                        "saldoEnCuenta": {
                            "type": "integer"
                        },
                        "totalTarjetasDeCreditoActualmente": {
                            "type": "integer"
                        },
                        "totalChequerasActualmente": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "estado",
                        "tipo",
                        "cuentaNumero",
                        "cupoDiarioRestante",
                        "cantidadExtraccionesHechas",
                        "monto",
                        "fecha",
                        "numero",
                        "saldoEnCuenta",
                        "totalTarjetasDeCreditoActualmente",
                        "totalChequerasActualmente"
                    ]
                }
            ]
        }
    },
    "required": [
        "numero",
        "nombre",
        "apellido",
        "dni",
        "tipo",
        "direccion",
        "transacciones"
    ]
}

def leerJSON(nombreJSON):
    with open(nombreJSON) as f:
        try:
            event = json.load(f)
            jsonschema.validate(event, schema)
            return event
        except ValidationError as e:
            print('Archivo JSON bien formateado pero no es válido:', e)
        except json.decoder.JSONDecodeError as e:
            print('Formato incorrecto, el archivo no es JSON:', e)