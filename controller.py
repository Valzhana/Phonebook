import model_search as s
import model_write as cr
import model_import as mod
import view


def button_click():
    action = view.select_action()
    phones = []
    if action == '1':
        act = view.search_method()
        if act == '1':
            phones = mod.get_number()
            cr.write_in_txt_column(phones)
        elif act == '2':
            phones = mod.get_number_line()
            cr.write_in_txt_line(phones)
        else:
            print('Error')
        cr.write_in_csv(phones)
    elif action == '2':
        cr.print_from_txt()
    elif action == '3':
        value = view.search_contact_by()
        s.search_by(value)
    else:
        print('Error')
