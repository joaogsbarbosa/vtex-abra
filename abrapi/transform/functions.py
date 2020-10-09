def filtrar(pedidos):
    # para cada pedido, criar um dict com cada atributo sendo uma tabela diferente
    pedidos_novos = []
    for pedido in pedidos:
        order = {
            "orderId": pedido["orderId"],
            "sequence": pedido["sequence"],
            "marketplaceOrderId": pedido["marketplaceOrderId"],
            "sellerOrderId": pedido["sellerOrderId"],
            "origin": pedido["origin"],
            "afffiliateId": pedido["affiliateId"],
            "salesChannel": pedido["salesChannel"],
            "merchantName": pedido["merchantName"],
            "status": pedido["status"],
            "statusDescription": pedido["statusDescription"],
            "value": pedido["value"],
            "creationDate": pedido["creationDate"],
            "lastChange": pedido["lastChange"],
            "orderGroup": pedido["orderGroup"],
            "followUpEmail": pedido["followUpEmail"],
            "roundingError": pedido["roundingError"],
            "orderFormId": pedido["orderFormId"],
            "isCompleted": pedido["isCompleted"],
            "allowCancellation": pedido["allowCancellation"],
            "allowEdition": pedido["allowEdition"],
            "isCheckedIn": pedido["isCheckedIn"],
            "authorizedData": pedido["authorizedDate"],
            "clientProfileData_id": pedido["clientProfileData"]["id"],
            "clientProfileData_email": pedido["clientProfileData"]["email"],
            "clientProfileData_firstName": pedido["clientProfileData"]["firstName"],
            "clientProfileData_lastName": pedido["clientProfileData"]["lastName"],
            "clientProfileData_documentType": pedido["clientProfileData"]["documentType"],
            "clientProfileData_phone": pedido["clientProfileData"]["phone"],
            "clientProfileData_userProfileId": pedido["clientProfileData"]["userProfileId"],
            "shippingData_id": pedido["shippingData"]["id"],
            "shippingData_address_addressType": pedido["shippingData"]["address"]["addressType"],
            "shippingData_address_receiverName": pedido["shippingData"]["address"]["receiverName"],
            "shippingData_address_addressId": pedido["shippingData"]["address"]["addressId"],
            "shippingData_address_postalCode": pedido["shippingData"]["address"]["postalCode"],
            "shippingData_address_city": pedido["shippingData"]["address"]["city"],
            "shippingData_address_state": pedido["shippingData"]["address"]["state"],
            "shippingData_address_street": pedido["shippingData"]["address"]["street"],
            "shippingData_address_number": pedido["shippingData"]["address"]["number"],
            "shippingData_address_neighborhood": pedido["shippingData"]["address"]["neighborhood"],
            "shippingData_address_complement": pedido["shippingData"]["address"]["complement"],
            "shippingData_address_reference": pedido["shippingData"]["address"]["reference"],
            "shippingData_address_country": pedido["shippingData"]["address"]["country"],
            "storePreferencesData_countryCode": pedido["storePreferencesData"]["countryCode"],
            "storePreferencesData_currencyCode": pedido["storePreferencesData"]["currencyCode"],
            "storePreferencesData_currencyLocale": pedido["storePreferencesData"]["currencyLocale"],
            "storePreferencesData_currencySymbol": pedido["storePreferencesData"]["currencySymbol"],
            "storePreferencesData_timeZone": pedido["storePreferencesData"]["timeZone"],
            "storePreferencesData_currencyFormatInfo_CurrencyDecimalDigits":
                pedido["storePreferencesData"]["currencyFormatInfo"]["CurrencyDecimalDigits"],
            "storePreferencesData_currencyFormatInfo_CurrencyDecimalSeparator":
                pedido["storePreferencesData"]["currencyFormatInfo"]["CurrencyDecimalSeparator"],
            "storePreferencesData_currencyFormatInfo_CurrencyGroupSeparator":
                pedido["storePreferencesData"]["currencyFormatInfo"]["CurrencyGroupSeparator"],
            "storePreferencesData_currencyFormatInfo_CurrencyGroupSize":
                pedido["storePreferencesData"]["currencyFormatInfo"]["CurrencyGroupSize"],
            "storePreferencesData_currencyFormatInfo_StartsWithCurrencySymbol":
                pedido["storePreferencesData"]["currencyFormatInfo"]["StartsWithCurrencySymbol"],
            "marketplace_baseURL": pedido["marketplace"]["baseURL"],
            "marketplace_isCertified": pedido["marketplace"]["isCertified"],
            "marketplace_name": pedido["marketplace"]["name"],
        }

        totals = []
        for total in pedido["totals"]:
            total_filtrado = {
                "id": total["id"],
                "name": total["name"],
                "value": total["value"],
                "orderId": order["orderId"],
            }
            totals.append(total_filtrado)

        items = []
        for item in pedido["items"]:
            item_filtrado = {
                "uniqueId": item["uniqueId"],
                "id": item["id"],
                "productId": item["productId"],
                "ean": item["ean"],
                "lockId": item["lockId"],
                "quantity": item["quantity"],
                "seller": item["seller"],
                "name": item["name"],
                "refId": item["refId"],
                "price": item["price"],
                "listPrice": item["listPrice"],
                "manualPrice": item["manualPrice"],
                "sellerSku": item["sellerSku"],
                "priceValidUntil": item["priceValidUntil"],
                "commission": item["commission"],
                "tax": item["tax"],
                "preSaleDate": item["preSaleDate"],
                "measurementUnit": item["measurementUnit"],
                "unitMultiplier": item["unitMultiplier"],
                "sellingPrice": item["sellingPrice"],
                "isGift": item["isGift"],
                "shippingPrice": item["shippingPrice"],
                "rewardValue": item["rewardValue"],
                "freightCommission": item["freightCommission"],
                "priceDefinitions": item["priceDefinitions"],
                "taxCode": item["taxCode"],
                "parentItemIndex": item["parentItemIndex"],
                "parentAssemblyBinding": item["parentAssemblyBinding"],
                "callCenterOperator": item["callCenterOperator"],
                "serialNumbers": item["serialNumbers"],
                "costPrice": item["costPrice"],
                "orderId": order["orderId"],
            }
            items.append(item_filtrado)

        sellers = []
        for seller in pedido["sellers"]:
            seller_filtrado = {
                "id": seller["id"],
                "name": seller["name"],
                "logo": seller["logo"],
                "fulfillmentEndpoint": seller["fulfillmentEndpoint"],
                "orderId": order["orderId"],
            }
            sellers.append(seller_filtrado)

        itemsMetadata = []
        for itemMetadata in pedido["itemMetadata"]["Items"]:
            itemMetaData_filtrado = {
                "Id": itemMetadata["Id"],
                "Seller": itemMetadata["Seller"],
                "Name": itemMetadata["Name"],
                "SkuName": itemMetadata["SkuName"],
                "ProductId": itemMetadata["ProductId"],
                "RefId": itemMetadata["RefId"],
                "Ean": itemMetadata["Ean"],
                "orderId": order["orderId"],
            }
            itemsMetadata.append(itemMetaData_filtrado)

        pedido_filtrado = {
            "order": [order],
            "totals": totals,
            "items": items,
            "sellers": sellers,
            "itemsMetadata": itemsMetadata,
        }
        pedidos_novos.append(pedido_filtrado)
    return pedidos_novos


def para_postgresql(pedidos):
    inserts = []
    for pedido in pedidos:
        for tabela in pedido:
            for linha in pedido[tabela]:
                chaves = ', '.join(map(str, linha.keys()))
                linha_values = [str(valor).replace("'", "''") for valor in linha.values()]
                valores = "'" + "','".join(linha_values) + "'"
                inserts.append('INSERT INTO "' + tabela +
                               '" (' + chaves + ')' + ' VALUES ' +
                               '(' + valores + ')' + ' ON CONFLICT DO NOTHING;')
    return inserts
