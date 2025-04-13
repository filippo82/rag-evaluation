"""RagEvaluation, a TUI for the evaluation of RAG systems."""

from pathlib import Path
import sys

if sys.version_info >= (3, 8):
    pass
else:
    pass

# try:
#    import httpx
# except ImportError:
#    raise ImportError("Please install httpx with 'pip install httpx' ")


from textual.containers import Container, Grid
from textual.app import App, ComposeResult, RenderResult
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Header, Footer, Button, Static

from rich.markdown import Markdown


class Home(Screen):
    """Home screen."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with Container(id="dialog"):
            yield Static(
                """ ____      _    ____                   _             _   _
|  _ \    / \  / ___|   _____   ____ _| |_   _  __ _| |_(_) ___  _ __
| |_) |  / _ \| |  _   / _ \ \ / / _` | | | | |/ _` | __| |/ _ \| '_ \\
|  _ <  / ___ \ |_| | |  __/\ V / (_| | | |_| | (_| | |_| | (_) | | | |
|_| \_\/_/   \_\____|  \___| \_/ \__,_|_|\__,_|\__,_|\__|_|\___/|_| |_|
""",
                classes="squirrel",
            )
            yield Static("Choose an option:", classes="question")
            yield Grid(
                Button("Query", id="query", variant="primary"),
                Button("Query parser", id="query_parser", variant="primary"),
                Button("Test1", id="test1", variant="primary"),
                Button("Widgets", id="widgets", variant="primary"),
                Button("Query", id="query2", variant="primary", disabled=True),
                Button("Monitoring", id="monitoring", variant="primary"),
                Button("Help", id="help", variant="primary", classes="help"),
                classes="buttons",
            )


class Help(Screen):
    """The help screen for the application."""

    BINDINGS = [("escape,space,q,question_mark", "pop_screen", "Close")]

    def compose(self) -> ComposeResult:
        """Compose the game's help.

        Returns:
            ComposeResult: The result of composing the help screen.
        """
        # yield Static(Markdown(Path(__file__).with_suffix(".md").read_text()))
        yield Header()
        yield Footer()
        yield Static(Markdown(Path("src/rag_evaluation/help.md").read_text()))


class Hello(Widget):
    """Display a greeting."""

    def render(self) -> RenderResult:
        return "Hello, [b]World[/b]!"


class Test1(Screen):
    """Test screen."""

    BINDINGS = [("h", "app.switch_screen('home')", "Home")]
    """Bindings for the help screen."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Hello()


# class Query(Screen):
#     """Query screen."""

#     BINDINGS = [
#         Binding("h", "app.switch_screen('home')", "Home"),
#         Binding("question_mark", "push_screen('help')", "Help", key_display="?"),
#         Binding("q", "quit", "Quit"),
#     ]
#     """The bindings for the main game grid."""

#     def compose(self) -> ComposeResult:
#         yield Header()
#         yield Footer()
#         yield Input(placeholder="Search ...")
#         yield VerticalScroll(Static(id="results"), id="results-container")

#     def on_mount(self) -> None:
#         """Called when app starts."""
#         # Give the input focus, so we can start typing straight away
#         self.query_one(Input).focus()

#     def on_input_submitted(self, message: Input.Changed) -> None:
#         """A coroutine to handle a text changed message."""
#         if message.value:
#             # Look up the word in the background
#             self.execute_query(message.value)
#         else:
#             # Clear the results
#             self.query_one("#results", Static).update()

#     def execute_query(self, query: str) -> None:
#         """Looks up a word."""
#         results = ...

#         # title = results["items"][0]["title"]
#         items = results["items"]

#         if query == self.query_one(Input).value:
#             markdown = self.make_result_list_markdown(items)
#             self.query_one("#results", Static).update(Markdown(markdown))
#             # self.query_one("#results", Static).update(title)

#     def make_result_list_markdown(self, items: object) -> str:
#         """Convert the results in to markdown."""
#         lines = []
#         # if isinstance(results, dict):
#         #     lines.append(f"# {results['title']}")
#         #     lines.append(results["message"])
#         if isinstance(items, list):
#             for item in items:
#                 log(item.keys())
#                 lines.append(f"# {item['title']}")
#                 lines.append("")
#                 lines.append(f"{item.get('abstract', 'Abstract not available')} ...")
#                 # for meaning in result.get("meanings", []):
#                 #     lines.append(f"_{meaning['partOfSpeech']}_")
#                 #     lines.append("")
#                 #     for definition in meaning.get("definitions", []):
#                 #         lines.append(f" - {definition['definition']}")
#                 #     lines.append("---")

#         return "\n".join(lines)


class RagEvaluation(App):
    """A Textual app for the evaluation of RAG systems."""

    CSS_PATH = "style.css"
    """The name of the stylesheet for the app."""

    SCREENS = {
        "home": Home,
        "help": Help,
        # "query": Query,
        "test1": Test1,
    }

    BINDINGS = [
        ("ctrl+d", "toggle_dark", "Toggle Dark Mode"),
        ("ctrl+q", "quit", "Quit"),
    ]

    TITLE = "RagEvaluation - a TUI for the evaluation of RAG systems"

    # def __init__(self) -> None:
    #     """Init."""

    def on_mount(self) -> None:
        """Set up the application on startup."""
        self.push_screen(Home())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed.

        Args:
            event (Button.Pressed): The event to react to.
        """
        button_id = event.button.id
        if button_id == "test1":
            self.push_screen("test1")
        elif button_id == "query":
            self.push_screen("query")
        elif button_id == "widgets":
            self.push_screen("widgets")
        elif button_id == "help":
            self.push_screen("help")
        elif button_id == "query_parser":
            self.push_screen("query_parser")


def main():
    print("ciao")
    app = RagEvaluation()
    print(app.run())


if __name__ == "__main__":
    main()
