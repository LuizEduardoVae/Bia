import streamlit as st

def main():
    st.title("Verificador de Status de Relacionamento")

    # Pergunta se a pessoa está solteira
    solteira = st.radio("Você está solteira?", ("Sim", "Não"))

    if solteira == "Sim":
        # Botão para exibir a pergunta de namoro
        if st.button("APERTE AQUI ENTAO"):
            st.write("💕 Quer namorar comigo? 💕")
    else:
        st.write("Que pena! 😔")

if __name__ == "__main__":
    main()
