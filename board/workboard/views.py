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

	return render_to_response('listSpecificPage.html', {'boardList': boardList, 
                                                            'totalCnt': totalCnt,
                                                            'current_page':current_page ,
                                                            'totalPageList':totalPageList} )

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
        if current_page=='':
            current_page=1

	current_row = (int(current_page)*rowsPerPage) - rowsPerPage
	boardList = workboard.objects.raw('select * from workboard_workboard \
                                           order by id desc limit %s, %s ', (current_row, rowsPerPage))
	pagingHelperIns = pagingHelper();
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
	print boardList
	print 'totalPageList',totalPageList
	
	return render_to_response('listSpecificPage.html',{'boardList':boardList,
                                                           'totalCnt':totalCnt,
                                                           'current_page':int(current_page),
                                                           'totalPageList':totalPageList})


def view_work(request):

    pk = request.GET['memo_id']
    board_data = workboard.objects.get(id = pk)
    workboard.objects.filter(id = pk).update(hits = board_data.hits +1)

    return render_to_response('view_memo.html',{'memo_id': request.GET['memo_id'],
                                                'current_page': request.GET['current_page'],
                                                'search_str': request.GET['search_str'],
                                                'board_data':board_data})


def list_searched_specific_page_work(request):

    search_str = request.GET['search_str']
    page_for_view = request.GET['page_for_view']
    
    total_cnt = workboard.objects.filter(subject__contains=searct_str).count()

    paging_helper_ins = pagingHelper();
    total_page_list = paging_helper_ins.getTotalPageList(total_cnt, rowsPerPage)

    current_row = (int(page_for_view)*rowsPerPage) - rowsPerPage
    board_list = workboard.objects.raw("select * from workboard_workboard \
                                        where subject like'%%'||%s||'%%' order by id desc\
                                        limit %s, %s",(search_str, current_row, rowsPerPage))

def list_specific_page_work_to_update(request):

    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    searchStr = request.GET['searchStr']
    board_data = workboard.objects.get(id= memo_id)

    return render_to_response('viewForUpdate.html',{'memo_id':request.GET['memo_id'],
                                                    'current_page':request.GET['current_page'],
                                                    'searchStr':request.GET['searchStr'],
                                                    'boardDate':board_date})


@csrf_exempt
def updateBoard(request):

    memo_id = request.POST['memo_id']
    current_page = request.POST['current_page']
    search_str = request.POST['searchStr']

    workboard.objects.filter(id= memo_id).update( mail= request.POST['mail'],subject= request.POST['subject'],memo= request.POST['memo'])
    url = '/listSpecificPageWork?current_page='+str(current_page)
    return HttpResponseRedirect(url)


