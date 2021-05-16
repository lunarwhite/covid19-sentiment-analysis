from pyecharts.charts import *
from pyecharts import options as opts

x_data = ['1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '2.1', '2.2', '2.3', '2.4',
          '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13', '2.14', '2.15', '2.16', '2.17', '2.18',
          '2.19', '2.20', '2.21', '2.22', '2.23', '2.24', '2.25', '2.26', '2.27', '2.28', '2.29', '3.1', '3.2', '3.3',
          '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13', '3.14', '3.15', '3.16', '3.17',
          '3.18', '3.19', '3.20', '3.21', '3.22', '3.23', '3.24', '3.25', '3.26', '3.27', '3.28', '3.29', '4.1',
          '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '4.10', '4.11', '4.12', '4.13', '4.14', '4.15',
          '4.16', '4.17', '4.18', '4.19', '4.20', '4.21', '4.22', '4.23', '4.24', '4.25', '4.26', '4.27', '4.28',
          '4.29', '4.30', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '5.10', '5.11', '5.12',
          '5.13', '5.14', '5.16', '5.17', '5.19', '5.21']
y_data = ['1.6603', '2.5563', '4.5729', '3.4913', '2.5449', '5.3985', '8.6268', '2.1630', '6.5072', '5.4547',
          '7.9366', '8.8279', '4.1944', '5.5686', '4.9844', '3.6430', '7.7520', '6.389', '8.1098', '11.6733',
          '12.511', '13.798', '14.737', '14.920', '12.918', '14.070', '15.005', '12.578', '17.061', '20.214',
          '12.306', '14.607', '13.210', '17.294', '17.447', '13.607', '13.943', '14.491', '12.779', '12.518',
          '16.384', '18.128', '14.142', '21.471', '19.741', '17.981', '13.543', '20.741', '19.639', '14.150',
          '16.301', '20.844', '17.600', '19.150', '17.706', '15.757', '18.763', '16.348', '15.628', '11.982',
          '14.324', '15.160', '14.607', '18.774', '11.905', '12.362', '15.129', '14.500', '12.834', '10.386',
          '11.085', '16.449', '13.841', '18.107', '13.717', '20.791', '12.752', '16.707', '17.018', '19.742',
          '15.426', '13.666', '15.037', '22.191', '10.412', '11.780', '13.689', '16.743', '11.731', '16.170',
          '16.016', '14.721', '20.828', '11.998', '18.726', '16.521', '18.165', '14.956', '15.365', '16.981',
          '18.408', '20.559', '14.723', '18.146', '12.334', '15.217', '20.612', '20.295', '18.132', '13.963',
          '11.723', '15.093', '11.682', '15.953', '19.827', '16.620']


def line_with_mark_area():
    line = Line(init_opts=opts.InitOpts(theme='essos', width='1600px', height='450px'))
    line.add_xaxis(x_data)
    line.add_yaxis('百天情感趋势图', y_data)

    # 设置标记区域
    line.set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            data=[
                opts.MarkAreaItem(name="情绪低落期", x=("1.20", "2.8"))
            ]
        )
    )
    return line

chart = line_with_mark_area()
chart.render('res\\output\\emotion-dict\\image\\百天折线图.html')
