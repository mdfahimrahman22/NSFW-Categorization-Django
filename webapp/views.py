from django.shortcuts import render, redirect
from webapp.models import RowTrack
from core.settings import ws, wb
# Create your views here.


def home(request):
    row = RowTrack.objects.first()
    current_index = row.current_index

    cell_img_url = 'D'+str(current_index)
    img_url = ws[cell_img_url].value
    cell_text = 'E'+str(current_index)
    img_text = ws[cell_text].value

    context = {
        'row': row,
        'img_url': img_url,
        'img_text': img_text,
    }
    if request.method == 'POST':
        cell_nsfw_category = 'K'+request.POST['row_index']
        category = request.POST['radio-btn-input']
        ws[cell_nsfw_category] = request.POST['radio-btn-input']
        wb.save('dataset/NSFW test 1.xlsx')
        row.current_index = int(request.POST['row_index'])+1
        if category == 'Pornography':
            row.pornography_count = row.pornography_count+1
        elif category == 'Misogyny':
            row.misogyny_count = row.misogyny_count+1
        elif category == 'Malignant Stereotypes':
            row.malignant_stereotypes_count = row.malignant_stereotypes_count+1
        elif category == 'Malign':
            row.malign_count = row.malign_count+1
        elif category == 'Delete':
            row.delete_count = row.delete_count+1
        row.save()
        return redirect('home')

    return render(request, 'index.html', context)
