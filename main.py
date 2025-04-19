from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class AgeApp(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.tab_height = 40

        # --- Onglet 1 : Devine ton âge ---
        self.age_tab = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.age_input = TextInput(hint_text="Année de naissance (ex: 2000)", multiline=False)
        self.age_result = Label(text="")
        age_button = Button(text="Calculer l'âge", size_hint=(1, 0.2))
        age_button.bind(on_press=self.calculer_age)
        self.age_tab.add_widget(self.age_input)
        self.age_tab.add_widget(age_button)
        self.age_tab.add_widget(self.age_result)
        self.add_widget(self._make_tab("Âge", self.age_tab))

        # --- Onglet 2 : Jours de vie ---
        self.jours_tab = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.jours_input = TextInput(hint_text="Date de naissance (JJ/MM/AAAA)", multiline=False)
        self.jours_result = Label(text="")
        jours_button = Button(text="Calculer les jours", size_hint=(1, 0.2))
        jours_button.bind(on_press=self.calculer_jours)
        self.jours_tab.add_widget(self.jours_input)
        self.jours_tab.add_widget(jours_button)
        self.jours_tab.add_widget(self.jours_result)
        self.add_widget(self._make_tab("Jours de vie", self.jours_tab))

    def _make_tab(self, title, content):
        from kivy.uix.tabbedpanel import TabbedPanelItem
        tab = TabbedPanelItem(text=title)
        tab.add_widget(content)
        return tab

    def calculer_age(self, instance):
        try:
            annee = int(self.age_input.text)
            age = datetime.now().year - annee
            self.age_result.text = f"Tu as {age} ans."
        except:
            self.age_result.text = "Année invalide."

    def calculer_jours(self, instance):
        try:
            date_str = self.jours_input.text
            naissance = datetime.strptime(date_str, "%d/%m/%Y")
            jours = (datetime.now() - naissance).days
            self.jours_result.text = f"Tu es en vie depuis {jours} jours."
        except:
            self.jours_result.text = "Date invalide. Utilise JJ/MM/AAAA."

class MonApp(App):
    def build(self):
        return AgeApp()

if __name__ == '__main__':
    MonApp().run()
