# -*- coding: UTF-8 -*-
"""
使用reportlab导出数据，生成一个表格
"""

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors


class PDFTable:

    def __init__(self, filename, pagesize=A4):
        self.doc = SimpleDocTemplate(filename, pagesize=pagesize, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        self.styles = getSampleStyleSheet()
        self.elements = list()
        self.table_data = list()
        self.columns = 0
        self.row = 0
        self.table_style = [
            ('TEXTCOLOR',(0,0),(1,-1),colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('GRID',(0,0), (-1,-1),1,colors.black),
            ('FONTSIZE',(0,0),(-1,-1),10),
            ('FONT', (0,0), (-1,-1), 'Times-Bold'),
            ('BOTTOMPADDING',(0,0),(-1,-1),2),
            ('TOPPADDING',(0,0),(-1,-1),2),
            ('SPAN', (0, 0), (0, 1)),          # 合并单元格 第一行第一个和第二行第一个
            ("SPAN", (1, 0), (1, 1))
        ]

        # [
        #     ('ALIGN', (1, 1), (-1, -1), "CENTER"),
        #     ('LINEABOVE', (0, 0), (-1, 0), 1, colors.purple),
        #     ('LINEBELOW', (0, 0), (-1, 0), 1, colors.purple),
        #     ('FONT', (0, 0), (-1, 0), 'Times-Bold')
        # ]

    def set_title(self, title=None):
        self.elements.append(Paragraph(title, self.styles['Title']))
    
    def set_table_head(self, head):
        """
        head: list or tuple
        """
        if isinstance(head, list) or isinstance(head, tuple):
            self.columns = len(head)
            self.table_data.append(head)
        else:
            raise ValueError("表头应该为列表或者元组")

    def set_table_body(self, body):
        if isinstance(body, list) or isinstance(body, tuple):
            self.row = len(body)
            
            if self.row > 0:
                if self.columns != len(body[0]):
                    raise Exception("表头和表体不对应")
            else:
                raise Exception("表体不能为空")

            self.table_data.extend(body)
        else:
            raise ValueError("表体应该为列表或者元组")

    def build(self):
        table = Table(self.table_data, style=self.table_style)
        self.elements.append(table)
        self.doc.build(self.elements)


if __name__ == "__main__":
    tab = PDFTable('./file/table01.pdf')
    tab.set_title("title")
    # tab.set_title(u'标题')
    tab.set_table_head(['name', 'age'])
    tab.set_table_head(["", ""])
    tab.set_table_body([
        ['xxx', 123],
        ['yyy', 124],
        ['zzz', 125]
    ])
    tab.build()