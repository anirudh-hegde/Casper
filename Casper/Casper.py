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


                xt.center(xt.text("YAML-2-PYTHON",
                        # margin_top="20px",
                        font_size="39px",
                        text_align="center",

                        color="violet",
                        ),),
                xt.link(
                    xt.image(src="/github.svg",
                             height="57px",
                             width="57px",
                             text_align="center",
                             align_items="center",
                             justify_content="center",
                             flex_direction="column",
                             margin_left="98em",
                             ),
                    is_external=True,
                    href="https://github.com/anirudh-hegde"
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
#
# # import yaml
# # import nextpy as xt
# #
# # import webbrowser
# #
# #
# # class State(xt.State):
# #     yaml_input: str = ""
# #     python_data: str = ""
# #
# #     def on_yaml_input_change(self, value):
# #         self.yaml_input = value
# #
# #     def convert_yaml_to_python(self):
# #         try:
# #             python_data = yaml.safe_load(self.yaml_input)
# #             if python_data:
# #                 self.python_data = f"{python_data}"
# #             else:
# #                 self.python_data = ""
# #         except yaml.YAMLError as e:
# #             self.python_data = f"Error parsing YAML: {e}"
# #
# #     def on_yaml_output_change(self, value):
# #         self.python_data = value
# #
# #     def handle_conversion(self):
# #         self.convert_yaml_to_python()
# #
# #
# # # def open_github():
# # #     webbrowser.open("https://github.com/anirudh-hegde")
# # #     return xt.
# # def index() -> xt.Component:
# #     layout = xt.fragment(
# #         xt.box(
# #
# #             xt.text("YAML-2-PYTHON",
# #                     font_size="43px",
# #                     text_align="center",
# #                     height="100%",
# #                     ),
# #             #
# #             bg="black",
# #             color="violet",
# #         ),
# #         xt.vstack(
# #             xt.center(
# #                 xt.hstack(
# #                     xt.vstack(
# #                         xt.text_area(
# #                             font_size="22px",
# #                             bg="black",
# #                             color="white",
# #                             placeholder="Paste YAML code here",
# #                             on_change=State.on_yaml_input_change,
# #                             width="100%",
# #                             height="500px",
# #                         ),
# #                     ),
# #                     xt.box(
# #                         spacing="4em",
# #                     ),
# #                     xt.vstack(
# #                         xt.button("Convert to Python code", on_click=State.handle_conversion),
# #                     ),
# #                     xt.box(
# #                         spacing="4em",
# #                     ),
# #                     xt.vstack(
# #                         xt.text_area(
# #                             color="white",
# #                             bg="black",
# #                             font_size="22px",
# #                             on_change=State.on_yaml_output_change,
# #                             value=State.python_data,
# #                             width="100%",
# #                             height="500px",
# #                         ),
# #                     ),
# #                 ),
# #             ),
# #             xt.button(
# #                 # xt.link("https://github.com/anirudh-hegde", ),
# #                 # on_click=lambda : open_github),
# #                 xt.image(
# #                     src="/github.svg",
# #                     height="30px",
# #                     width="30px",
# #                     padding_right='1px',
# #                     target="https://github.com/anirudh-hegde"
# #                 ),
# #             ),
# #             align_items="center",
# #             justify_content="center",
# #             height="100vh",
# #             background="linear-gradient(to top, #30cfd0 0%, #330867 100%)",
# #         ),
# #     )
# #
# #     return layout
# #
# #
# # app = xt.App()
# # app.add_page(index)
#
# import yaml
# import nextpy as xt
# import webbrowser
#
#
# class State(xt.State):
#     yaml_input: str = ""
#     python_data: str = ""
#
#     def on_yaml_input_change(self, value):
#         self.yaml_input = value
#
#     def convert_yaml_to_python(self):
#         try:
#             python_data = yaml.safe_load(self.yaml_input)
#             if python_data:
#                 self.python_data = f"{python_data}"
#             else:
#                 self.python_data = ""
#         except yaml.YAMLError as e:
#             self.python_data = f"Error parsing YAML: {e}"
#
#     def on_yaml_output_change(self, value):
#         self.python_data = value
#
#     def handle_conversion(self):
#         self.convert_yaml_to_python()
#
#
# def open_github():
#     webbrowser.open("https://github.com/anirudh-hegde")
#     return xt.no_update()
#
#
# def index() -> xt.Component:
#     layout = xt.fragment(
#         xt.box(
#             xt.link(
#                 xt.image(
#                     src="/github.svg",
#                     height="30px",
#                     width="30px",
#                     padding_right='1px'
#                 ),
#                 href="https://github.com/anirudh-hegde"
#             ),
#             bg="black",
#             color="violet",
#         ),
#         xt.vstack(
#             xt.center(
#                 xt.hstack(
#                     xt.vstack(
#                         xt.text_area(
#                             font_size="22px",
#                             bg="black",
#                             color="white",
#                             placeholder="Paste YAML code here",
#                             on_change=State.on_yaml_input_change,
#                             width="100%",
#                             height="500px",
#                         ),
#                     ),
#                     xt.box(
#                         spacing="4em",
#                     ),
#                     xt.vstack(
#                         xt.button("Convert to Python code", on_click=State.handle_conversion),
#                     ),
#                     xt.box(
#                         spacing="4em",
#                     ),
#                     xt.vstack(
#                         xt.text_area(
#                             color="white",
#                             bg="black",
#                             font_size="22px",
#                             on_change=State.on_yaml_output_change,
#                             value=State.python_data,
#                             width="100%",
#                             height="500px",
#                         ),
#                     ),
#                 ),
#             ),
#             align_items="center",
#             justify_content="center",
#             height="100vh",
#             background="linear-gradient(to top, #30cfd0 0%, #330867 100%)"
#
#         ),
#     )
#
#     return layout
#
#
# app = xt.App()
# app.add_page(index)
