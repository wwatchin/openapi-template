APISPEC = ./openapi/apispec.yaml
TEMPLATE_DIR = ./openapi/templates
TEMPLATES = $(addprefix $(TEMPLATE_DIR)/, main.jinja2)

UVICORN_IP = localhost
UVICORN_PORT = 8000

ifeq ($(OS),Windows_NT)
PYTHON = python
RM = del
else
PYTHON = python3
RM = rm
endif

all: run

run: main.py
	$(PYTHON) -m uvicorn main:app --host $(UVICORN_IP) --port $(UVICORN_PORT)

clean:
	$(RM) main.py models.py

main.py: $(APISPEC) $(TEMPLATES)
	fastapi-codegen -i $(APISPEC) -t $(TEMPLATE_DIR) -o .
	sed -i "s/from .models/from models/" $@

.PHONY: run clean
