def clearAllWidgets(targetLayout):
    for i in reversed(range(targetLayout.count())):
        comp = targetLayout.takeAt(i).widget()
        if comp is not None:
            comp.deleteLater()
