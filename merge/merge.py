import PyPDF2


def merge_pdfs横向(horizontal, pdfs):
    # 创建一个PDF写入器对象
    pdf_writer = PyPDF2.PdfWriter()

    # 遍历所有PDF文件
    for pdf in pdfs:
        # 打开每个PDF文件
        with open(pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # 获取第一个PDF的页面对象
            if len(pdf_writer.pages) == 0:
                first_page = pdf_reader.pages[0]
                # 将页面旋转90度以实现横向合并
                first_page.rotateCounterClockwise(90)
                pdf_writer.addPage(first_page)

            # 将其他PDF的页面添加到写入器
            for page in pdf_reader.pages:
                # 将页面旋转90度以实现横向合并
                page.rotateCounterClockwise(90)
                pdf_writer.addPage(page)

    # 将合并后的PDF保存到新文件
    with open('merged.pdf', 'wb') as out_file:
        pdf_writer.write(out_file)


# 调用函数横向合并PDF
merge_pdfs横向(90,['bandwidth-latency-dram.pdf', 'bandwidth-latency-dram.pdf'])