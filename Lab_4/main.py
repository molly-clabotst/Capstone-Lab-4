from view import View
from view_model import ViewModel
from database import SQLJugglerDB

# MAIN
def main():
    db_jugglers = SQLJugglerDB
    jugglers_view_model = ViewModel(db_jugglers)
    View.make_menu(jugglers_view_model)

if __name__ == '__main__':
    main()