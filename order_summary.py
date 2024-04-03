from py_pdf_parser.loaders import load_file
from py_pdf_parser import tables

# from py_pdf_parser.visualise import visualise


# Step 1 - Load the file
document = load_file("order_summary.pdf")

# visualise(document)

# Step 2 - Use a font mapping

# Show all fonts:
# set(element.font for element in document.elements)

FONT_MAPPING = {
    "BAAAAA+LiberationSerif-Bold,16.0": "title",
    "BAAAAA+LiberationSerif-Bold,12.0": "sub_title",
    "CAAAAA+LiberationSerif,12.0": "text",
    "DAAAAA+FreeMonoBold,12.0": "table_header",
    "EAAAAA+FreeMono,12.0": "table_text",
}
document = load_file("order_summary.pdf", font_mapping=FONT_MAPPING)

# OR

# use regex patterns

FONT_MAPPING = {
    r"\w{6}\+LiberationSerif-Bold,16.0": "title",
    r"\w{6}\+LiberationSerif-Bold,12.0": "sub_title",
    r"\w{6}\+LiberationSerif,12.0": "text",
    r"\w{6}\+FreeMonoBold,12.0": "table_header",
    r"\w{6}\+FreeMono,12.0": "table_text",
}
document = load_file("order_summary.pdf", font_mapping=FONT_MAPPING, font_mapping_is_regex=True)

# visualise(document)

# Step 3 - Add sections
order_summary_sub_title_element = (
    document.elements.filter_by_font("sub_title")
    .filter_by_text_equal("Order Summary:")
    .extract_single_element()
)

totals_sub_title_element = (
    document.elements.filter_by_font("sub_title")
    .filter_by_text_equal("Totals:")
    .extract_single_element()
)

final_element = document.elements[-1]

order_summary_section = document.sectioning.create_section(
    name="order_summary",
    start_element=order_summary_sub_title_element,
    end_element=totals_sub_title_element,
    include_last_element=False,
)

totals_section = document.sectioning.create_section(
    name="totals", start_element=totals_sub_title_element, end_element=final_element
)

# visualise(document)

# Step 4 - Extract tables

order_summary_table = tables.extract_simple_table(
    order_summary_section.elements.filter_by_fonts("table_header", "table_text"),
    as_text=True,
)

totals_table = tables.extract_simple_table(
    totals_section.elements.filter_by_fonts("table_header", "table_text"), as_text=True
)

order_summary_with_header = tables.add_header_to_table(order_summary_table)

print(order_summary_table)
print(order_summary_with_header)