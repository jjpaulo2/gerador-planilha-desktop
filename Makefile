# ----------------------------------------
# MAKEFILE PARA AUXILIAR PROCESSO DE BUILD
# FEITO POR @jjpaulo2
# ----------------------------------------

# VARIÁVEIS DE BUILD DO PROJETO
APPNAME 	 = "gerador-planilhas-desktop"
APPFILE		 = app.py

# -----------------------------------------------------------
# AO EXECUTAR `make` OU `make help` SERÁ EXECUTADO ESTE BLOCO
# -----------------------------------------------------------
help:
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "	make prepare .............. instala as dependências do projeto"
	@echo "	make binary ............... gera o executável com PyInstaller"
	@echo "	make all .................. instala as dependências e depois gera o executável"
	@echo ""


# ---------------------------------------------------
# INSTRUÇÕES PARA INSTALAR AS DEPENDÊNCIAS DO PROJETO
# ---------------------------------------------------
prepare:
	@echo ""
	@echo "Instalando dependências..."
	@echo ""

	@python -m pip install --upgrade --user pipenv
	@echo ""

	@python -m pipenv install


# --------------------------------------------------------
# INSTRUÇÕES PARA GERAR OS BINÁRIOS DO SISTEMA OPERACIONAL
# --------------------------------------------------------
binary:
	@echo ""
	@echo "Gerando binário do sistema..."
	@echo ""

	@python -m pipenv run \
		pyinstaller --onefile --windowed \
		--name $(APPNAME) \
		$(APPFILE)

	@echo ""
	@echo "Acesse a pasta ./dist para ver o executável."
	@echo ""


# -----------------------------------------------------------
# EXECUTA OS COMANDOS `make prepare` E `make binary` EM ORDEM
# -----------------------------------------------------------
all:
	@make prepare
	@make binary
