import os
import PySimpleGUI as sg
from src.GeneratorAlgorithm import GeneratorAlgorithm
from datetime import datetime

sg.LOOK_AND_FEEL_TABLE["CPFGen"] = {
    'BACKGROUND': "white",
    'TEXT': "#323232",
    'INPUT': "#dfe2e8",
    'TEXT_INPUT': '#000000',
    'SCROLL': '#c7e78b',
    'BUTTON': ("white", "#db0000"),
    'PROGRESS': ("white", "black"),
    'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
}

sg.change_look_and_feel("CPFGen")

main_layout = [
    [sg.Text("\n", font=("Segoe UI Light", 5))],
    [sg.Text("  Gerador de CPFs", justification="left", font=("Segoe UI Light", 24), text_color="#db0000")],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text("    Saída do arquivo:", font=("Segoe UI Light", 14)), sg.InputText(f"{os.getcwd()}", size=(28, 6), font=("Segoe UI Light", 12)), sg.VerticalSeparator(pad=(7, 5)), sg.FolderBrowse("Procurar", size=(10, 0), font=("Segoe UI", 10))],
    [sg.Text("    Quantos CPFs deseja gerar?", font=("Segoe UI Light", 14)), sg.InputText(size=(18, 6), font=("Segoe UI Light", 12)), sg.VerticalSeparator(pad=(6, 5)), sg.Submit("Gerar CPFs", size=(10, 0), font=("Segoe UI", 10))],
    [sg.Text("\n    Desenvolvido por Pedro Lemos (@pedrolemoz)", font=("Segoe UI Light", 12), size=(42, 0), justification="center")]
]

window = sg.Window("Gerador de CPFs", main_layout, size=(555, 250), icon="icon.ico")

while True:
    event, values = window.read()
    if event == None:
        break

    if event == "Gerar CPFs":
        try:
            filename = f"{values[1]} CPFs - {datetime.now().strftime('%c')}.txt".replace(":", "-")
            path = values[0]

            with open(os.path.join(path, filename), "a") as file:
                file.write("=" * 45 + " AVISO " + "=" * 45 + f"\n\n\nEstes {values[1]} CPFs foram gerados aleatoriamente por um programa automatizado.\nO intuito dessa ferramenta é fornecer dados fictícios para realização de testes.\nA má utilização dos CPFs gerados por esse script é de total responsabilidade do utilizador.\nÉ possível também que existam CPFs válidos dentre os que foram gerados.\nFerramenta criada por Pedro Lemos, e disponível em: https://github.com/pedrolemoz/geradordecpf\nGerado em: {datetime.now().strftime('%c')}\n\n\n")

                waiting_layout = [
                    [sg.Text("\n", font=("Segoe UI Light", 5))],
                    [sg.Text("  Gerando os CPFs, aguarde", font=("Segoe UI Light", 14))],
                    [sg.Text("\n", font=("Segoe UI Light", 1))],
                    [sg.Text(" " * 31), sg.Button("Cancelar", size=(12, 0), font=("Segoe UI", 10))],
                    [sg.Text("\n", font=("Segoe UI Light", 1))]
                ]

                waiting_window = sg.Window("Aguarde", waiting_layout, auto_close=True)
                cancel_operation = False

                CPF = GeneratorAlgorithm()
                for i in range(int(values[1])):
                    file.write(f"{CPF.generate_CPF()}\n")

                    waiting_event, waiting_value = waiting_window.read()

                    if waiting_event == "Cancelar":
                        cancel_operation = True
                        waiting_window.close()
                        break

            if cancel_operation == False:
                sucess_layout = [
                    [sg.Text("\n", font=("Segoe UI Light", 5))],
                    [sg.Text(f"  {values[1]} CPFs gerados com sucesso!\n", font=("Segoe UI Light", 14))],
                    [sg.Text(" " * 9), sg.Button("Ver pasta de saída", size=(18, 0), font=("Segoe UI", 10)), sg.Button("Fechar", size=(10, 0), font=("Segoe UI", 10))],
                    [sg.Text("\n", font=("Segoe UI Light", 1))]
                ]

                sucess_window = sg.Window("Sucesso!", sucess_layout)

                while True:
                    sucess_event, sucess_value = sucess_window.read()
                    
                    if sucess_event in (None, "Fechar"):
                        sucess_window.close()
                        break

                    elif sucess_event == "Ver pasta de saída":
                        os.startfile(path)
            else:
                failure_layout = [
                    [sg.Text("\n", font=("Segoe UI Light", 5))],
                    [sg.Text("  Operação cancelada pelo usuário", font=("Segoe UI Light", 14))],
                    [sg.Text("\n", font=("Segoe UI Light", 1))],
                    [sg.Text(" " * 44), sg.Button("Voltar", size=(12, 0), font=("Segoe UI", 10))],
                    [sg.Text("\n", font=("Segoe UI Light", 1))]
                ]

                failure_window = sg.Window("Operação cancelada", failure_layout, size=(340, 140))

                while True:
                    failure_event, failure_value = failure_window.read()
                    
                    if failure_event in (None, "Voltar"):
                        failure_window.close()
                        break

        except ValueError:
            sg.PopupError("Insira apenas números inteiros", title="Erro de valor", font=("Helvetica", 12))
        
        except FileNotFoundError:
            sg.PopupError("Diretório inválido", title="Erro de diretório", font=("Helvetica", 12))

window.close()
