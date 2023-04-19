from django.shortcuts import render, get_object_or_404, redirect	
from .models import Post, Category, Comment

def home(request):
	return render(request, 'blog/index.html')

def post(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def category(request):
	categorys = Category.objects.all()
	return render(request, 'blog/post_list.html', {'categorys': categorys})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)

	if request.method == 'POST':
		name = request.POST.get('name', '')
		comment = request.POST.get('comment', '')

		if name and comment:
			Comment.objects.create(
				post=post,
				name=name,
				comment=comment
			)

			return redirect('post_detail', slug=post.slug)

	return render(request, 'blog/detail.html', {'post': post})