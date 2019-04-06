import markup
import info_table

# Link
web_label = markup.label_start_markup + "info" + markup.label_end_markup
web_link = markup.text_start_markup + "<a href='http://huayra.conectarigualdad.gob.ar/'>sitio web</a>" + markup.text_end_markup


info_table.add_row_to_table(web_label, web_link, 8, destino="gui")
