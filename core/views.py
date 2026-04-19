from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

# a) Inserir novo registro
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'core/criar.html', {'form': form})

# b) Listar os registros
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/listar.html', {'produtos': produtos})

# c) Buscar
def buscar_produto(request):
    query = request.GET.get('q', '')
    produtos = Produto.objects.filter(nome__icontains=query) if query else Produto.objects.all()
    return render(request, 'core/listar.html', {'produtos': produtos, 'query': query})

# d) Editar
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'core/editar.html', {'form': form, 'produto': produto})

# e) Deletar
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'core/deletar.html', {'produto': produto})
