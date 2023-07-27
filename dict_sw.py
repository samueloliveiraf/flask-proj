
sw_create = {
    "tags": ["API Endpoints"],
    "summary": "Create a new company",
    "securityDefinitions": {
        "basicAuth": {
            "type": "basic"
        }
    },
    "security": [{
        "basicAuth": []
    }],
    "description": "Receives a JSON with the company's information, validates the "
                   "CNPJ and saves the company in the database. Returns a JSON with a success or error message.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Company's information",
            "required": True,
            "schema": {
                "id": "company_data",
                "required": ["name_company", "name_fantasy", "cnpj", "cnae"],
                "properties": {
                    "name_company": {
                        "type": "string",
                        "description": "Company's name"
                    },
                    "name_fantasy": {
                        "type": "string",
                        "description": "Company's trade name"
                    },
                    "cnpj": {
                        "type": "string",
                        "description": "Company's CNPJ"
                    },
                    "cnae": {
                        "type": "string",
                        "description": "Company's CNAE"
                    },
                }
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Company successfully created",
            "schema": {
                "id": "success_response",
                "properties": {
                    "success": {
                        "type": "string",
                        "description": "Success message"
                    },
                }
            },
        },
        "400": {
            "description": "Error creating company",
            "schema": {
                "id": "error_response",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    },
                }
            },
        }
    }
}

sw_list = {
    "tags": ["API Endpoints"],
    "summary": "List all companies",
    "securityDefinitions": {
        "basicAuth": {
            "type": "basic"
        }
    },
    "security": [{
        "basicAuth": []
    }],
    "description": "Get a list of all companies, with support for pagination, "
                   "ordering and limiting the number of records per page.",
    "parameters": [
        {
            "name": "page",
            "in": "query",
            "type": "integer",
            "required": False,
            "description": "Page number for pagination, starting from 1.",
            "default": 1
        },
        {
            "name": "limit",
            "in": "query",
            "type": "integer",
            "required": False,
            "description": "Number of records per page.",
            "default": 10
        },
        {
            "name": "order",
            "in": "query",
            "type": "string",
            "required": False,
            "description": "Field by which to order the companies.",
            "default": "name_company"
        },
    ],
    "responses": {
        "200": {
            "description": "A list of companies",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name_company": {
                            "type": "string",
                            "description": "Company's name"
                        },
                        "name_fantasy": {
                            "type": "string",
                            "description": "Company's trade name"
                        },
                        "cnpj": {
                            "type": "string",
                            "description": "Company's CNPJ"
                        },
                        "cnae": {
                            "type": "string",
                            "description": "Company's CNAE"
                        },
                    },
                }
            },
        }
    }
}

sw_edit = {
    "tags": ["API Endpoints"],
    "summary": "Edit an existing company",
    "securityDefinitions": {
        "basicAuth": {
            "type": "basic"
        }
    },
    "security": [{
        "basicAuth": []
    }],
    "description": "Receives a JSON with the CNPJ of the company to edit and the new "
                   "trade name and/or CNAE, validates the information and updates "
                   "the company in the database. Returns a JSON with a success or error message.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Data to edit",
            "required": True,
            "schema": {
                "id": "edit_data",
                "required": ["cnpj"],
                "properties": {
                    "cnpj": {
                        "type": "string",
                        "description": "Company's CNPJ"
                    },
                    "name_fantasy": {
                        "type": "string",
                        "description": "New trade name (optional)"
                    },
                    "cnae": {
                        "type": "string",
                        "description": "New CNAE (optional)"
                    },
                }
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Company successfully updated",
            "schema": {
                "id": "success_response",
                "properties": {
                    "success": {
                        "type": "string",
                        "description": "Success message"
                    },
                }
            },
        },
        "400": {
            "description": "Error updating company",
            "schema": {
                "id": "error_response",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    },
                }
            },
        }
    }
}

sw_delete = {
    "tags": ["API Endpoints"],
    "summary": "Delete an existing company",
    "securityDefinitions": {
        "basicAuth": {
            "type": "basic"
        }
    },
    "security": [{
        "basicAuth": []
    }],
    "description": "Receives a JSON with the CNPJ of the company to delete, validates the CNPJ and "
                   "deletes the company from the database. Returns a JSON with a success or error message.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Data to delete",
            "required": True,
            "schema": {
                "id": "delete_data",
                "required": ["cnpj"],
                "properties": {
                    "cnpj": {
                        "type": "string",
                        "description": "Company's CNPJ"
                    },
                }
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Company successfully deleted",
            "schema": {
                "id": "success_response",
                "properties": {
                    "success": {
                        "type": "string",
                        "description": "Success message"
                    },
                }
            },
        },
        "400": {
            "description": "Error deleting company",
            "schema": {
                "id": "error_response",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    },
                }
            },
        }
    }
}
