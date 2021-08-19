def filtrar(pedidos):
    pedidos_novos = []
    for pedido in pedidos:
        pedido_filtrado = {}
        try:
            order = {
                "orderId": pedido["orderId"] if 'orderId' in pedido else None,
                "sequence": pedido["sequence"] if 'sequence' in pedido else None,
                "marketplaceOrderId": pedido["marketplaceOrderId"] if 'marketplaceOrderId' in pedido else None,
                "marketplaceServicesEndpoint": pedido["marketplaceServicesEndpoint"] if 'marketplaceServicesEndpoint' in pedido else None,
                "sellerOrderId": pedido["sellerOrderId"] if 'sellerOrderId' in pedido else None,
                "origin": pedido["origin"] if 'origin' in pedido else None,
                "afffiliateId": pedido["affiliateId"] if 'affiliateId' in pedido else None,
                "salesChannel": pedido["salesChannel"] if 'salesChannel' in pedido else None,
                "merchantName": pedido["merchantName"] if 'merchantName' in pedido else None,
                "status": pedido["status"] if 'status' in pedido else None,
                "statusDescription": pedido["statusDescription"] if 'statusDescription' in pedido else None,
                "value": pedido["value"] if 'value' in pedido else None,
                "creationDate": pedido["creationDate"] if 'creationDate' in pedido else None,
                "lastChange": pedido["lastChange"] if 'lastChange' in pedido else None,
                "orderGroup": pedido["orderGroup"] if 'orderGroup' in pedido else None,
                "callCenterOperatorData": pedido["callCenterOperatorData"] if 'callCenterOperatorData' in pedido else None,
                "followUpEmail": pedido["followUpEmail"] if 'followUpEmail' in pedido else None,
                "hostname": pedido["hostname"] if 'hostname' in pedido else None,
                "roundingError": pedido["roundingError"] if 'roundingError' in pedido else None,
                "orderFormId": pedido["orderFormId"] if 'orderFormId' in pedido else None,
                "commercialConditionData": pedido["commercialConditionData"] if 'commercialConditionData' in pedido else None,
                "isCompleted": pedido["isCompleted"] if 'isCompleted' in pedido else None,
                "allowCancellation": pedido["allowCancellation"] if 'allowCancellation' in pedido else None,
                "allowEdition": pedido["allowEdition"] if 'allowEdition' in pedido else None,
                "isCheckedIn": pedido["isCheckedIn"] if 'isCheckedIn' in pedido else None,
                "authorizedDate": pedido["authorizedDate"] if 'authorizedDate' in pedido else None,
                "invoicedDate": pedido["invoicedDate"] if 'invoicedDate' in pedido else None,
                "cancelReason": pedido["cancelReason"] if 'cancelReason' in pedido else None,
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
                "openTextField_value": pedido["openTextField"]["value"] if pedido["openTextField"] else None,
            }
            if 'marketplace' in pedido and pedido["marketplace"] is not None:
                order["marketplace_baseURL"] = pedido["marketplace"]["baseURL"] if 'baseURL' in pedido["marketplace"] else None
                order["marketplace_isCertified"] = pedido["marketplace"]["isCertified"] if 'isCertified' in pedido["marketplace"] else None
                order["marketplace_name"] = pedido["marketplace"]["name"] if 'name' in pedido["marketplace"] else None
            if 'marketingData' in pedido and pedido["marketingData"] is not None:
                order["marketingData_id"] = pedido["marketingData"]["id"] if 'id' in pedido["marketingData"] else None
                order["marketingData_utmSource"] = pedido["marketingData"]["utmSource"] if 'utmSource' in pedido["marketingData"] else None
                order["marketingData_utmPartner"] = pedido["marketingData"]["utmPartner"] if 'utmPartner' in pedido["marketingData"] else None
                order["marketingData_utmMedium"] = pedido["marketingData"]["utmMedium"] if 'utmMedium' in pedido["marketingData"] else None
                order["marketingData_utmCampaign"] = pedido["marketingData"]["utmCampaign"] if 'utmCampaign' in pedido["marketingData"] else None
                order["marketingData_coupon"] = pedido["marketingData"]["coupon"] if 'coupon' in pedido["marketingData"] else None
                order["marketingData_utmiCampaign"] = pedido["marketingData"]["utmiCampaign"] if 'utmiCampaign' in pedido["marketingData"] else None
                order["marketingData_utmipage"] = pedido["marketingData"]["utmipage"] if 'utmipage' in pedido["marketingData"] else None
                order["marketingData_utmiPart"] = pedido["marketingData"]["utmiPart"] if 'utmiPart' in pedido["marketingData"] else None
        except Exception as e:
            print("[Erro] Objeto order - "+pedido["orderId"])
            print("Detalhes do erro:", e)
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
            except Exception as e:
                print("[Erro] Objeto totals - " + order["orderId"])
                print("Detalhes do erro:", e)
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
            except Exception as e:
                print("[Erro] Objeto items - " + order["orderId"])
                print("Detalhes do erro:", e)
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
            except Exception as e:
                print("[Erro] Objeto sellers -" + order["orderId"])
                print("Detalhes do erro:", e)
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
            except Exception as e:
                print("[Erro] Objeto itemsMetaData - " + order["orderId"])
                print("Detalhes do erro:", e)
            else:
                pedido_filtrado["itemsMetadata"] = itemsmetadata

            try:
                paymentData_transactions_payments = []
                for paymentData_transactions in pedido["paymentData"]["transactions"]:
                    for payment in paymentData_transactions["payments"]:
                        payment_filtrado = {
                            "id": payment["id"] if payment["id"] else '',
                            "paymentSystem": payment["paymentSystem"],
                            "paymentSystemName": payment["paymentSystemName"],
                            "value": payment["value"],
                            "installments": payment["installments"],
                            "referenceValue": payment["referenceValue"],
                            "orderId": order["orderId"],
                        }
                        paymentData_transactions_payments.append(payment_filtrado)
            except Exception as e:
                print("[Erro] Objeto paymentData_transactions_payments - " + order["orderId"])
                print("Detalhes do erro:", e)
            else:
                pedido_filtrado["paymentData_transactions_payments"] = paymentData_transactions_payments

            try:
                ratesAndBenefitsData_rateAndBenefitsIdentifiers = []
                for rateAndBenefitsIdentifier in pedido["ratesAndBenefitsData"]["rateAndBenefitsIdentifiers"]:
                    rateAndBenefitsIdentifiers_filtrado = {
                        "id": rateAndBenefitsIdentifier["id"] if 'id' in rateAndBenefitsIdentifier else None,
                        "name": rateAndBenefitsIdentifier["name"] if 'name' in rateAndBenefitsIdentifier else None,
                        "matchedParameters_paymentMethodId": rateAndBenefitsIdentifier["matchedParameters"]["paymentMethodId"] if 'paymentMethodId' in rateAndBenefitsIdentifier["matchedParameters"] else None,
                        "matchedParameters_couponCodeMarketing": rateAndBenefitsIdentifier["matchedParameters"]["couponCode@Marketing"] if 'couponCode@Marketing' in rateAndBenefitsIdentifier["matchedParameters"] else None,
                        "orderId": order["orderId"],
                    }
                    ratesAndBenefitsData_rateAndBenefitsIdentifiers.append(rateAndBenefitsIdentifiers_filtrado)
            except Exception as e:
                print("[Erro] Objeto ratesAndBenefitsData_rateAndBenefitsIdentifiers -" + order["orderId"])
                print("Detalhes do erro:", e)
            else:
                pedido_filtrado["ratesAndBenefitsData_rateAndBenefitsIdentifiers"] = ratesAndBenefitsData_rateAndBenefitsIdentifiers

            try:
                if 'packages' in pedido["packageAttachment"]:
                    packageAttachment_packages = []
                    for package in pedido["packageAttachment"]["packages"]:
                        package_filtrado = {
                            "courier": package["courier"] if 'courier' in package else None,
                            "invoiceNumber": package["invoiceNumber"] if 'invoiceNumber' in package else None,
                            "invoiceValue": package["invoiceValue"] if 'invoiceValue' in package else None,
                            "issuanceDate": package["issuanceDate"] if 'issuanceDate' in package else None,
                            "orderId": order["orderId"],
                        }
                        if 'courierStatus' in package and package["courierStatus"] is not None:
                            package_filtrado["courierStatus_status"] = package["courierStatus"]["status"] if 'status' in package["courierStatus"] else None
                            package_filtrado["courierStatus_finished"] = package["courierStatus"]["finished"] if 'finished' in package["courierStatus"] else None
                            package_filtrado["courierStatus_deliveredDate"] = package["courierStatus"]["deliveredDate"] if 'deliveredDate' in package["courierStatus"] else None
                        packageAttachment_packages.append(package_filtrado)
                    pedido_filtrado["packageAttachment_packages"] = packageAttachment_packages
            except Exception as e:
                print("[Erro] Objeto packageAttachment_packages -" + order["orderId"])
                print("Detalhes do erro:", e)

            try:
                shippingData_logisticsInfo = []
                for logisticInfo in pedido["shippingData"]["logisticsInfo"]:
                    logisticInfo_filtrado = {
                        "itemIndex": logisticInfo["itemIndex"],
                        "price": logisticInfo["price"],
                        "listPrice": logisticInfo["listPrice"],
                        "sellingPrice": logisticInfo["sellingPrice"],
                        "shippingEstimate": logisticInfo["shippingEstimate"],
                        "shippingEstimateDate": logisticInfo["shippingEstimateDate"],
                        "orderId": order["orderId"],
                    }
                    shippingData_logisticsInfo.append(logisticInfo_filtrado)
            except Exception as e:
                print("[Erro] Objeto shippingData_logisticsInfo -" + order["orderId"])
                print("Detalhes do erro:", e)
            else:
                pedido_filtrado["shippingData_logisticsInfo"] = shippingData_logisticsInfo

            pedidos_novos.append(pedido_filtrado)

    return pedidos_novos


def para_mysql(pedidos):
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
                inserts.append('REPLACE INTO `' + tabela +
                               '` (' + chaves + ')' + ' VALUES ' +
                               '(' + valores + ')')
    return inserts
