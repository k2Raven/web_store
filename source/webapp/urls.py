from django.urls import path
from webapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CartView, ProductsAddToCartView, \
    ProductsRemoveFromCartView, ProductsRemoveFromCartPieceByPieceView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('cart/', CartView.as_view(), name='cart_list'),
    path('products/<int:pk>/add-to-cart/', ProductsAddToCartView.as_view(), name='products-add-to-cart'),
    path('cart/<int:pk>/delete/', ProductsRemoveFromCartView.as_view(), name='products-remove-from-cart'),
    path('cart/<int:pk>/delete_piece_by_piece/', ProductsRemoveFromCartPieceByPieceView.as_view(),
         name='products-remove-from-cart_piece_by_piece'),
]
