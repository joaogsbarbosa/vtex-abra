def filtrar(pedidos):
    pedidos_novos = []
    for pedido in pedidos:
        pedido_filtrado = {}
        try:
            order = {
                "orderId": pedido["orderId"],
                "sequence": pedido["sequence"],
                "marketplaceOrderId": pedido["marketplaceOrderId"],
                "marketplaceServicesEndpoint": pedido["marketplaceServicesEndpoint"],
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
                "giftRegistryData": pedido["giftRegistryData"],
                "callCenterOperatorData": pedido["callCenterOperatorData"],
                "followUpEmail": pedido["followUpEmail"],
                "hostname": pedido["hostname"],
                "roundingError": pedido["roundingError"],
                "orderFormId": pedido["orderFormId"],
                "commercialConditionData": pedido["commercialConditionData"],
                "isCompleted": pedido["isCompleted"],
                "allowCancellation": pedido["allowCancellation"],
                "allowEdition": pedido["allowEdition"],
                "isCheckedIn": pedido["isCheckedIn"],
                "authorizedDate": pedido["authorizedDate"],
                "invoicedDate": pedido["invoicedDate"],
                "cancelReason": pedido["cancelReason"],
                "clientProfileData_id": pedido["clientProfileData"]["id"],
                "clientProfileData_email": pedido["clientProfileData"]["email"],
                "clientProfileData_firstName": pedido["clientProfileData"]["firstName"],
                "clientProfileData_lastName": pedido["clientProfileData"]["lastName"],
                "clientProfileData_documentType": pedido["clientProfileData"]["documentType"],
                "clientProfileData_document": pedido["clientProfileData"]["document"],
                "clientProfileData_phone": pedido["clientProfileData"]["phone"],
                "clientProfileData_corporateName": pedido["clientProfileData"]["corporateName"],
                "clientProfileData_tradeName": pedido["clientProfileData"]["tradeName"],
                "clientProfileData_corporateDocument": pedido["clientProfileData"]["corporateDocument"],
                "clientProfileData_stateInscription": pedido["clientProfileData"]["stateInscription"],
                "clientProfileData_corporatePhone": pedido["clientProfileData"]["corporatePhone"],
                "clientProfileData_isCorporate": pedido["clientProfileData"]["isCorporate"],
                "clientProfileData_userProfileId": pedido["clientProfileData"]["userProfileId"],
                "clientProfileData_customerClass": pedido["clientProfileData"]["customerClass"],
                "ratesAndBenefitsData_id": pedido["ratesAndBenefitsData"]["id"],
                "shippingData_id": pedido["shippingData"]["id"],
                "shippingData_address_addressType": pedido["shippingData"]["address"]["addressType"],
                "shippingData_address_receiverName": pedido["shippingData"]["address"]["receiverName"],
                "shippingData_address_addressId": pedido["shippingData"]["address"]["addressId"],
                "shippingData_address_postalCode": pedido["shippingData"]["address"]["postalCode"],
                "shippingData_address_city": pedido["shippingData"]["address"]["city"],
                "shippingData_address_state": pedido["shippingData"]["address"]["state"],
                "shippingData_address_country": pedido["shippingData"]["address"]["country"],
                "shippingData_address_street": pedido["shippingData"]["address"]["street"],
                "shippingData_address_number": pedido["shippingData"]["address"]["number"],
                "shippingData_address_neighborhood": pedido["shippingData"]["address"]["neighborhood"],
                "shippingData_address_complement": pedido["shippingData"]["address"]["complement"],
                "shippingData_address_reference": pedido["shippingData"]["address"]["reference"],
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
        except:
            print("[Erro] Objeto order - Erro")
        else:
            pedido_filtrado["order"] = [order]

            # Se não ocorrer problemas para transformar "order", então transformar os restantes
            try:
                totals = []
                for total in pedido["totals"]:
                    total_filtrado = {
                        "id": total["id"],
                        "name": total["name"],
                        "value": total["value"],
                        "orderId": order["orderId"],
                    }
                    totals.append(total_filtrado)
            except:
                print("[Erro] Objeto totals - " + order["orderId"])
            else:
                pedido_filtrado["totals"] = totals

            try:
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
                        "taxCode": item["taxCode"],
                        "parentItemIndex": item["parentItemIndex"],
                        "parentAssemblyBinding": item["parentAssemblyBinding"],
                        "callCenterOperator": item["callCenterOperator"],
                        "serialNumbers": item["serialNumbers"],
                        "costPrice": item["costPrice"],
                        "orderId": order["orderId"],
                    }
                    items.append(item_filtrado)
            except:
                print("[Erro] Objeto items - " + order["orderId"])
            else:
                pedido_filtrado["items"] = items

            try:
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
            except:
                print("[Erro] Objeto sellers -" + order["orderId"])
            else:
                pedido_filtrado["sellers"] = sellers

            try:
                itemsmetadata = []
                for itemMetadata in pedido["itemMetadata"]["Items"]:
                    itemmetadata_filtrado = {
                        "Id": itemMetadata["Id"],
                        "Seller": itemMetadata["Seller"],
                        "Name": itemMetadata["Name"],
                        "SkuName": itemMetadata["SkuName"],
                        "ProductId": itemMetadata["ProductId"],
                        "RefId": itemMetadata["RefId"],
                        "Ean": itemMetadata["Ean"],
                        "orderId": order["orderId"],
                    }
                    itemsmetadata.append(itemmetadata_filtrado)
            except:
                print("[Erro] Objeto itemsMetaData - " + order["orderId"])
            else:
                pedido_filtrado["itemsMetadata"] = itemsmetadata

            pedidos_novos.append(pedido_filtrado)

    return pedidos_novos


def para_postgresql(pedidos):
    inserts = []
    for pedido in pedidos:
        for tabela in pedido:
            for linha in pedido[tabela]:
                chaves = ', '.join(map(str, linha.keys()))
                valores = []
                for valor in linha.values():
                    if valor is None:
                        valor = "NULL"
                    else:
                        valor = str(valor).replace("'", "''")
                        valor = "'" + valor + "'"
                    valores.append(valor)
                valores = ",".join(valores)
                inserts.append('INSERT INTO "' + tabela +
                               '" (' + chaves + ')' + ' VALUES ' +
                               '(' + valores + ')' + ' ON CONFLICT DO NOTHING;')
    return inserts
