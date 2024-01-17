import yaml
import nextpy as xt


class State(xt.State):
    yaml_input: str = ""
    python_data: str = ""

    def on_yaml_input_change(self, value):
        self.yaml_input = value

    def convert_yaml_to_python(self):
        try:
            python_data = yaml.safe_load(self.yaml_input)
            if python_data:
                self.python_data = f"{python_data}"
            else:
                self.python_data = ""
        except yaml.YAMLError as e:
            self.python_data = f"Error parsing YAML: {e}"

    def on_yaml_output_change(self, value):
        self.python_data = value

    def handle_conversion(self):
        self.convert_yaml_to_python()


def index() -> xt.Component:
    layout = xt.fragment(

        xt.box(

            xt.hstack(
                xt.text("YAML-2-PYTHON",
                        margin_left="4em",
                        font_size="40px",
                        text_align="center",
                        color="violet",
                        ),

                xt.link(
                    xt.image(src="/github.svg",
                             height="39px",
                             width="39px",
                             # text_align="center",
                             align_items="center",
                             justify_content="center",
                             flex_direction="column",
                             margin_left="68em",
                             ),
                    is_external=True,
                    href="https://github.com/anirudh-hegde/Casper",
                ),

            ),
            bg="black",
            height="100%",
            align_items="center",
            justify_content="center",

        ),
        xt.vstack(
            xt.center(
                xt.hstack(
                    xt.vstack(
                        xt.text_area(
                            font_size="22px",
                            bg="black",
                            color="white",
                            placeholder="Paste YAML code here",
                            on_change=State.on_yaml_input_change,
                            width="100%",
                            height="500px",

                        ),
                    ),
                    # xt.spacer()
                    xt.box(
                        spacing="4em",
                    ),
                    xt.vstack(
                        xt.button("Convert to Python code", on_click=State.handle_conversion, ),
                    ),

                    xt.box(
                        spacing="4em",
                    ),
                    xt.vstack(
                        xt.text_area(
                            color="white",
                            bg="black",
                            font_size="22px",
                            on_change=State.on_yaml_output_change,
                            value=State.python_data,
                            width="100%",
                            height="500px",
                        ),
                    ),

                ),
            ),
            align_items="center",
            justify_content="center",
            height="100vh",
            # line_height="8px",
            background="linear-gradient(to top, #30cfd0 0%, #330867 100%)"
        ),

    )
    return layout


app = xt.App()
app.add_page(index)
