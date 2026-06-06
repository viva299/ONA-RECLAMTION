import flet as ft

def main(page: ft.Page):
    # 1. إعدادات النافذة (حجم الهاتف)
    page.window_width = 400
    page.window_height = 700
    page.title = "شكاوى ONA"
    page.rtl = True 
    page.scroll = ft.ScrollMode.AUTO

    # 2. الألوان المستخدمة (أكواد سداسية لتجنب أخطاء المكتبة)
    ona_green = "#8CC63F"
    ona_blue = "#0054A6"

    # 3. العناصر (بدون تعقيدات)
    logo = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Logo_ONA.jpg/320px-Logo_ONA.jpg",
        width=120,
    )
    
    txt_name = ft.TextField(label="الاسم واللقب", border_color=ona_blue)
    txt_address = ft.TextField(label="العنوان", border_color=ona_blue)
    txt_phone = ft.TextField(label="رقم الهاتف", border_color=ona_blue)
    
    status_text = ft.Text("الحالة: جاهز للإرسال")

    def submit_complaint(e):
        status_text.value = "تم إرسال الشكوى بنجاح!"
        page.update()

    # 4. إضافة العناصر
    page.add(
        ft.Column(
            [
                logo,
                ft.Text("تقديم شكوى المواطن", size=20, weight="bold"),
                txt_name,
                txt_address,
                txt_phone,
                ft.ElevatedButton("تحديد الموقع", icon="gps_fixed"),
                ft.ElevatedButton("إرفاق صورة", icon="camera_alt"),
                ft.Divider(),
                ft.FilledButton("إرسال الشكوى", on_click=submit_complaint, style=ft.ButtonStyle(bgcolor=ona_green)),
                status_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# تشغيل التطبيق في المتصفح هو الخيار الأكثر استقراراً لتجنب الشاشة البيضاء
ft.app(target=main, view=ft.AppView.WEB_BROWSER)