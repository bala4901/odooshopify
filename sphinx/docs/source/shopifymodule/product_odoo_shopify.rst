.. _OdooShopifyProduct:

#################
Products
#################

.. _OdooShopifySyncProducts:

Product [Odoo] yang ready untuk Upload ke Shopify
========================================================

Menu ``Shopify > Products > Products``

Di sini kita bisa bisa melihat product yang telah kita buat dari odoo melalui :ref:`Export Product`.
Data-data di sini hampir persis sama menu yang di shopify. Di sini bisa kita edit
dan ntar di syncron lagi sama shopify.

| Di menu ini terdapat 2 bagian ``Shopify Info`` dan ``Variants``

.. figure:: ../images/s_product_barcode_notebook.png
   :align: center
   :class: with-border

.. _ShopifyInfo:

Shopify Info
------------

.. figure:: ../images/o_shopify_product.png
   :align: center
   :class: with-border

.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Fields
      - Description
    * - Instance
      - Website Shopify mana yang di pakai untuk sync
    * - Exported In Shopify
      - Ini akan di centang bila sudah upload ke shopify
    * - Shopify Tmpl Id
      - Ini akan muncul bila sudah sukses upload ke shopify
    * - Product Template
      - Product odoo yang di pakai. :ref:`Export Product`
    * - Tags
      - Tags untuk product ini. Input :ref:`Product Tags`
    * - Inventory Management
      - Option:
         * Shopify tracks this product Inventory
         * Don't Tracks Inventory
    * - Sale Out of stock products?
      - Bila Inventory Management (Shopify tracks this product inventory), barang yang tidak ada stock tidak akan terjual di Shopify
    * - Taxable
      - Apakah perlu Pajak
    * - Description
      - Ini bisa di tulis berupa Text atau HTML dan update ke shopify


Variants
------------

| Variants adalah variasi dalam 1 Product.
| Contoh: T-shirt Spider-man adalah Product. Karena T-shirt itu ada Warna dan ukuran.
| T-Shirt Spider-man - Merah, Kuning, Hijau s, etc, smua ini ada variants nya.
| 
| Kita bisa tambah atau kurangin variant yang akan di update ke Shopify.

.. figure:: ../images/o_shopify_product_variants.png
   :align: center
   :class: with-border