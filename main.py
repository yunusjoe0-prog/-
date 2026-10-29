from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math


class ScientificCalculatorApp(App):

    def build(self):
        self.title = "Casio Scientific Calculator"
        self.expression = ""

        # تخطيط الشاشة الرئيسي
        root_layout = BoxLayout(
            orientation="vertical", padding=10, spacing=10
        )

        # شاشة العرض
        self.display = TextInput(
            font_size=32,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=(0.06, 0.12, 0.08, 1),
            foreground_color=(0.0, 1.0, 0.4, 1),
        )
        root_layout.add_widget(self.display)

        # صفوف الأزرار للآلة الحاسبة العلمية
        buttons = [
            ["sin", "cos", "tan", "√", "^"],
            ["log", "ln", "π", "e", "%"],
            ["(", ")", "x²", "C", "DEL"],
            ["7", "8", "9", "÷", "!"],
            ["4", "5", "6", "×", "1/x"],
            ["1", "2", "3", "-", "="],
            ["0", ".", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                btn = Button(
                    text=label,
                    font_size=20,
                    background_normal="",
                    background_color=self.get_button_color(label),
                )
                btn.bind(on_press=self.on_button_click)
                h_layout.add_widget(btn)
            root_layout.add_widget(h_layout)

        return root_layout

    def get_button_color(self, label):
        # ألوان مخصصة لكل نوع زر (تصميم فني وعصري)
        if label in ["C", "DEL"]:
            return (0.6, 0.1, 0.1, 1)  # أحمر للمسح
        elif label == "=":
            return (0.04, 0.4, 0.25, 1)  # أخضر للنتيجة
        elif label in ["sin", "cos", "tan", "√", "log", "ln", "x²", "!", "1/x"]:
            return (0.12, 0.2, 0.3, 1)  # أزرق داكن للدوال
        elif label in ["+", "-", "×", "÷", "^", "(", ")", "%", "π", "e"]:
            return (0.2, 0.2, 0.2, 1)  # رمادي للعمليات
        else:
            return (0.15, 0.15, 0.15, 1)  # رمادي غامق للأرقام

    def on_button_click(self, instance):
        text = instance.text

        if text == "C":
            self.expression = ""
        elif text == "DEL":
            self.expression = self.expression[:-1]
        elif text == "=":
            try:
                # معالجة العمليات الحسابية لتتوافق مع بايثون
                exp = (
                    self.expression.replace("×", "*")
                    .replace("÷", "/")
                    .replace("^", "**")
                )
                exp = exp.replace("π", str(math.pi)).replace(
                    "e", str(math.e)
                )

                # حساب الأقواس المفقودة تلقائياً
                open_b = exp.count("(")
                close_b = exp.count(")")
                if open_b > close_b:
                    exp += ")" * (open_b - close_b)

                result = str(eval(exp))
                self.expression = result
            except Exception:
                self.expression = "Error"
        elif text == "√":
            self.expression += "math.sqrt("
        elif text in ["sin", "cos", "tan"]:
            self.expression += f"math.{text}(math.radians("
        elif text == "log":
            self.expression += "math.log10("
        elif text == "ln":
            self.expression += "math.log("
        elif text == "x²":
            self.expression += "**2"
        elif text == "!":
            self.expression += "math.factorial("
        elif text == "1/x":
            self.expression += "1/("
        else:
            self.expression += text

        self.display.text = self.expression


if __name__ == "__main__":
    ScientificCalculatorApp().run()
