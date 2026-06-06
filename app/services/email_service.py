from fastapi_mail import ConnectionConfig
from fastapi_mail import FastMail
from fastapi_mail import MessageSchema
from fastapi_mail import MessageType

conf = ConnectionConfig(
    MAIL_USERNAME="pedidos.graficapergaminho@gmail.com",
    MAIL_PASSWORD="xzioiijxzwutdvrk",
    MAIL_FROM="pedidos.graficapergaminho@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)

async def enviar_email_pedido(
    assunto: str,
    destinatario: str,
    corpo: str,
):

    mensagem = MessageSchema(
        subject=assunto,
        recipients=[destinatario],
        body=corpo,
        subtype=MessageType.plain,
    )

    fm = FastMail(conf)

    await fm.send_message(mensagem)