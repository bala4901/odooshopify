###############################
Shopify Operation
###############################

.. toctree::
   :maxdepth: 0
   :caption: Contents:

.. _ShopifyProductOverview:

***************************
Overview
***************************

Menu ``Shopify > Processess > Shopify Operations``


.. _ShopifyToOdoo:

*********************************
Shopify ke Odoo | Shopify ==> ERP
*********************************

.. figure:: ../images/shopify_operation.png
   :align: center
   :class: with-border

   *Figure: Shopify > Processess > Shopify Operations*


.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Fields
      - Description
    * - Import Orders
      - Import orderan dari Shopify
    * - Import Collections
      - Import Collections dan Tags dari Shopify
    * - Sync Product
      - Sync Product yang ada di Shopify dengan :ref:`OdooShopifySyncProducts` 
        dan juga untuk Sync barang Shopify yang tidak ada di odoo dengan 
        catatan ``Barcode`` di *Shopify* dan ``Ean13`` di *Odoo* harus sama.


.. _OdooToShopify:

*****************************************
Odoo ke Shopify | Odoo ==> Shopify
*****************************************

.. figure:: ../images/shopify_operation_toshopify.png
   :align: center
   :class: with-border

   *Figure: Shopify > Processess > Shopify Operations*


.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Fields
      - Description
    * - Export Products
      - Upload :ref:`OdooShopifyProduct` ke Shopify
    * - Publish Product
      - Barang yang di upload ke Shopify dan Ready untuk di Publish untuk show ke customer di online
    * - Update Product
      - Untuk update product odoo ke shopify
    * - Update Stock
      - Update Inventory odoo ke shopify
    * - Update Price
      - Update Price odoo ke shopify
    * - Update Order Status
      - Update Order Fulfilment ke Shopify
    * - Export Collections
      - Upload :ref:`ProductCollections` ke shopify
    * - Update Collection
      - Update collection ke shopify
    * - Publish Collection
      - Untuk publish collection jadi bisa di lihat oleh customer di online