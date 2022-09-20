from django.shortcuts import render,redirect
from webapp.models import RowTrack
from core.settings import ws, wb
# Create your views here.


def home(request):
    row = RowTrack.objects.first()
    current_index = row.current_index

    cell_img_url = 'D'+str(current_index)
    img_url = ws[cell_img_url].value

    context = {
        'row_index': current_index,
        'img_url': img_url
    }
    if request.method == 'POST':
        cell_nsfw_category = 'K'+request.POST['row_index']
        ws[cell_nsfw_category] = request.POST['radio-btn-input']
        wb.save('dataset/NSFW test 1.xlsx')
        row.current_index = int(request.POST['row_index'])+1
        row.save()
        return redirect('home')
        
    return render(request, 'index.html', context)
