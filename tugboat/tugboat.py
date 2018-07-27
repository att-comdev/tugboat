#/usr/bin/python
from excel_parser.generate_intermediary import GenerateIntermediary
from baremetal_processor.baremetal_processor import BaremeralProcessor


file_name = '{}{}'.format('/root/pk5294/gitrepos/tugboat/tugboat/schemas/',
                          'MTN_57_AEC_Design_Specs_v_1.1.xlsx')
excel_specs = 'excel_parser/config/excel_spec.yaml'
ob = GenerateIntermediary(file_name, excel_specs)
ob.generate_yaml()
ob1 = BaremeralProcessor('intermediary.yaml')
ob1.render_template('rack.yaml.j2')
