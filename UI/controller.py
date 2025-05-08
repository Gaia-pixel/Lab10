import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        a = int(self._view._txtAnno.value)
        if a is None or a == "":
            self._view.create_alert("Inserire l'anno'")
            return
        if a < 1816 or a > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("L'anno deve essere tra il 1816 e il 2016"))
            self._view.update_page()
            return

        self._model.build_graph(a)
        numNodi = self._model.getNumNodes()
        numArchi = self._model.getNumEdges()
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi: {numNodi}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi: {numArchi}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di componenti connesse: {self._model.getNumConnesse()}"))
        for stato in self._model.grafo:
            self._view._txt_result.controls.append(ft.Text(f"Stato: {stato} -- numero confinanti: {self._model.getNumeroConfinanti(stato)}"))


        self._view.update_page()



