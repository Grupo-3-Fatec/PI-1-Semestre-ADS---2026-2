from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


# =========================
# CONFIG
# =========================

TOKEN = "Insira o token"


# =========================
# START
# =========================


#assim que da o comando /start no telegram
#o telegram envia uma mensagem junto com os botoes clicaveis

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    botoes = [
        [
            InlineKeyboardButton(
                "Criar Planilha",
                callback_data="criar_planilha"
            )
        ],
        [
            InlineKeyboardButton(
                "Filtrar Dados da Planilha",
                callback_data="dados_Planilha"
            )
        ],
        [
            InlineKeyboardButton(
                "Retornar requisições da Planilha",
                callback_data="requisicoes_planilha"
            )
        ],
        [
            InlineKeyboardButton(
                "Eliminar Riscos de Compliance",
                callback_data="risco_compliance"
            )
        ],
        [
            InlineKeyboardButton(
                "Cumprimento de Metas",
                callback_data="metas"
            )
        ],
    ]


    teclado = InlineKeyboardMarkup(botoes)

#aqui esta a mensagem inicial que o bot vai enviar
#que contem o que contem a ação de cada botao assim que o apertalo

    await update.message.reply_text(
        "Olá! Seja bem-vindo ao nosso atendimento.\n"
        "Para começar, selecione uma das opções abaixo:\n \n"
        
        "CRIAR PLANILHA\n \n"

        "FILTRAR DADOS\n"
        "Filtre os dados desejados\n \n"


        "RETORNAR REQUISIÇÕES DA PLANILHA\n"
        "Buscar na planilha as requisições que foram registradas e mostrar.\n \n"

        "ELIMINAR RISCOS DE COMPLIANCE\n"
        "Evitar situações que façam a empresa descumprir regras\n \n"

        "CUMPRIMENTO DE METAS\n \n",
        
        reply_markup=teclado
    )


# =========================
# BOTÕES
# =========================


#aqui seria para o codigo identificar qual botao foi pressionado

async def botao_clicado(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


# =========================
# INICIAR BOT
# =========================

#aqui é onde define o comando de start (que pode ser alterado)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(botao_clicado)
)

app.run_polling()