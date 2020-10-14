create table "order" (
  orderId varchar(255),
  sequence varchar(255),
  marketplaceOrderId varchar(255),
  marketplaceServicesEndpoint varchar(255),
  sellerOrderId varchar(255),
  origin varchar(255),
  afffiliateId varchar(255),
  salesChannel varchar(255),
  merchantName varchar(255),
  status varchar(255),
  statusDescription varchar(255),
  value varchar(255),
  creationDate varchar(255),
  lastChange varchar(255),
  orderGroup varchar(255),
  giftRegistryData varchar(255),
  marketingData varchar(255),
  callCenterOperatorData varchar(255),
  followUpEmail varchar(255),
  hostname varchar(255),
  roundingError varchar(255),
  orderFormId varchar(255),
  commercialConditionData varchar(255),
  isCompleted varchar(255),
  allowCancellation varchar(255),
  allowEdition varchar(255),
  isCheckedIn varchar(255),
  authorizedDate varchar(255),
  invoicedDate varchar(255),
  cancelReason varchar(255),
  clientProfileData_id varchar(255),
  clientProfileData_email varchar(255),
  clientProfileData_firstName varchar(255),
  clientProfileData_lastName varchar(255),
  clientProfileData_documentType varchar(255),
  clientProfileData_document varchar(255),
  clientProfileData_phone varchar(255),
  clientProfileData_corporateName varchar(255),
  clientProfileData_tradeName varchar(255),
  clientProfileData_corporateDocument varchar(255),
  clientProfileData_stateInscription varchar(255),
  clientProfileData_corporatePhone varchar(255),
  clientProfileData_isCorporate varchar(255),
  clientProfileData_userProfileId varchar(255),
  clientProfileData_customerClass varchar(255),
  shippingData_id varchar(255),
  shippingData_address_addressType varchar(255),
  shippingData_address_receiverName varchar(255),
  shippingData_address_addressId varchar(255),
  shippingData_address_postalCode varchar(255),
  shippingData_address_city varchar(255),
  shippingData_address_state varchar(255),
  shippingData_address_country varchar(255),
  shippingData_address_street varchar(255),
  shippingData_address_number varchar(255),
  shippingData_address_neighborhood varchar(255),
  shippingData_address_complement varchar(255),
  shippingData_address_reference varchar(255),
  storePreferencesData_countryCode varchar(255),
  storePreferencesData_currencyCode varchar(255),
  storePreferencesData_currencyLocale varchar(255),
  storePreferencesData_currencySymbol varchar(255),
  storePreferencesData_timeZone varchar(255),
  storePreferencesData_currencyFormatInfo_CurrencyDecimalDigits varchar(255),
  storePreferencesData_currencyFormatInfo_CurrencyDecimalSeparator varchar(255),
  storePreferencesData_currencyFormatInfo_CurrencyGroupSeparator varchar(255),
  storePreferencesData_currencyFormatInfo_CurrencyGroupSize varchar(255),
  storePreferencesData_currencyFormatInfo_StartsWithCurrencySymbol varchar(255),
  marketplace_baseURL varchar(255),
  marketplace_isCertified varchar(255),
  marketplace_name varchar(255),
  primary key (orderId)
);

create table "items" (
  uniqueId varchar(255),
  id varchar(255),
  productId varchar(255),
  ean varchar(255),
  lockId varchar(255),
  quantity varchar(255),
  seller varchar(255),
  name varchar(255),
  refId varchar(255),
  price varchar(255),
  listPrice varchar(255),
  manualPrice varchar(255),
  sellerSku varchar(255),
  priceValidUntil varchar(255),
  commission varchar(255),
  tax varchar(255),
  preSaleDate varchar(255),
  measurementUnit varchar(255),
  unitMultiplier varchar(255),
  sellingPrice varchar(255),
  isGift varchar(255),
  shippingPrice varchar(255),
  rewardValue varchar(255),
  freightCommission varchar(255),
  priceDefinitions varchar(255),
  taxCode varchar(255),
  parentItemIndex varchar(255),
  parentAssemblyBinding varchar(255),
  callCenterOperator varchar(255),
  serialNumbers varchar(255),
  costPrice varchar(255),
  orderId varchar(255)
);

create table "totals" (
  id varchar(255),
  name varchar(255),
  value varchar(255),
  orderId varchar(255)
);

create table "sellers" (
  id varchar(255),
  name varchar(255),
  logo varchar(255),
  fulfillmentEndpoint varchar(255),
  orderId varchar(255)
);

create table "itemsMetadata" (
  Id varchar(255),
  Seller varchar(255),
  Name varchar(255),
  SkuName varchar(255),
  ProductId varchar(255),
  RefId varchar(255),
  Ean varchar(255),
  orderId varchar(255)
);