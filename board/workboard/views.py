# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from workboard.models import workboard
from workboard.pagingHelper import pagingHelper


rowsPerPage = 2

'''@csrf_exempt'''
def home(request):

	boardList = workboard.objects.order_by('-id')[0:2]
	current_page = 1
	totalCnt = workboard.objects.all().count()
	pagingHelperIns = pagingHelper();
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
	print 'totalPageList', totalPageList

	return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'current_page':current_page ,'totalPageList':totalPageList} )

def show_write_form(request):

	return render_to_response('writeBoard.html')

@csrf_exempt
def DoWriteBoard(request):

	br = workboard(subject = request.POST['subject'],
	name = request.POST['name'],
	mail = request.POST['email'],
	memo = request.POST['memo'],
	created_date = timezone.now(),
	hits = 0
)
	br.save()

	url = '/listSpecificPageWork?current_page=1'
	return HttpResponseRedirect(url)

def listSpecificPageWork(request):
	current_page = request.GET['current_page']
	totalCnt = workboard.objects.all().count()

	print 'current_page=',current_page
        current_row = (int(current_page)*rowsPerPage) - rowsPerPage

        '''
	boardList = workboard.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil( @rownum / %s ) as page FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS
                                         FROM workboard_workboard ORDER BY ID DESC ) X ) Z WHERE page = %s', [rowsPerPage, current_page])
        '''
        boardList = workboard.objects.raw('select * from workboard_workboard order by id desc limit %s, %s ', (current_row, rowsPerPage))
	pagingHelperIns = pagingHelper();
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
        print boardList
	print 'totalPageList',totalPageList
	return render_to_response('listSpecificPage.html',{'boardList':boardList,'totalCnt':totalCnt,'current_page':int(current_page),'totalPageList':totalPageList})


def view_work(request):

    pk = request.GET['memo_id']
    board_data = workboard.objects.get(id = pk)
    workboard.objects.filter(id = pk).update(hits = board_data.hits +1)

    return render_to_response('view_memo.html',{'memo_id': request.GET['memo_id'],
                                                'current_page': request.GET['current_page'],
                                                'search_str': request.GET['search_str'],
                                                'board_data':board_data})
