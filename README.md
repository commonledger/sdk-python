# sdk-ruby

Official CommonLedger API library client for ruby

__This library is generated by [alpaca](https://github.com/pksunkara/alpaca)__

## Installation

Make sure you have [pip](https://pypi.python.org/pypi/pip) installed

```bash
$ pip install commonledger-sdk
```

#### Versions

Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Usage

```python
import common_ledger

# Then we instantiate a client (as shown below)
```

### Build a client

##### Without any authentication

```python
client = common_ledger.Client()

# If you need to send options
client = common_ledger.Client({}, options)
```

##### Basic authentication

```python
auth = { 'username': 'pksunkara', 'password': 'password' }

client = common_ledger.Client(auth, options)
```

##### Oauth acess token

```python
client = common_ledger.Client('1a2b3', options)
```

##### Oauth client secret

```python
auth = { 'client_id': '09a8b7', 'client_secret': '1a2b3' }

client = common_ledger.Client(auth, options)
```

### Response information

```python
response = client.klass('args').method('args')

response.body
# >>> 'Hello world!'

response.code
# >>> 200

response.headers
# >>> {'content-type': 'text/html'}
```
##### HTML response

```python
response.body
# >>> 'The username is pksunkara!'
```

##### JSON response

```python
response.body
# >>> {'user': 'pksunkara'}
```

### Request body information

##### RAW request

```python
body = 'username=pksunkara'
```

##### FORM request

```python
body = {'user': 'pksunkara'}
```

##### JSON request

```python
body = {'user': 'pksunkara'}
```

### Client Options

The following options are available while instantiating a client:

 * __base__: Base url for the api
 * __api_version__: Default version of the api (to be used in url)
 * __user_agent__: Default user-agent for all requests
 * __headers__: Default headers for all requests
 * __request_type__: Default format of the request body

### Method Options

The following options are available while calling a method of an api:

 * __api_version__: Version of the api (to be used in url)
 * __headers__: Headers for the request
 * __query__: Query parameters for the url
 * __body__: Body of the request
 * __request_type__: Format of the request body

### Accounts api

Manages data relating to the Chart of Accounts

The following arguments are required:

 * __account_id__: The account UUID

```python
accounts = client.accounts("75e6a24c-772b-11e3-8005-6163636f756e")
```

##### Add account (POST /core.account/add)

Creates a new account in the chart of accounts

The following arguments are required:

 * __organisation_id__: The organisation the account belongs to
 * __account_number__: The account code
 * __name__: The account name
 * __classification__: The account classification
 * __type__: The type of classification for the account
 * __tax__: The tax code that applies to the account
 * __currency__: The currency code that applies to the account

```python
response = accounts.add("863f2548-7284-11e3-9710-6163636f756e", "200", "Business Tax Account 1", "ASSET", "BANK", "NONE", "NZD", options)
```

##### View account (GET /core.account/view/:account_id)





```python
response = accounts.view(options)
```

##### Update account (POST /core.account/update/:account_id)

Updates an existing account in the chart of accounts

The following arguments are required:

 * __organisation_id__: The organisation the account belongs to
 * __account_number__: The account code
 * __name__: The account name
 * __classification__: The account classification
 * __type__: The type of classification for the account
 * __tax__: The tax code that applies to the account
 * __currency__: The currency code that applies to the account

```python
response = accounts.update("863f2548-7284-11e3-9710-6163636f756e", "200", "Business Tax Account 1", "ASSET", "BANK", "NONE", "NZD", options)
```

##### Delete account (GET /core.account/delete/:account_id)

Deletes an account from the chart of accounts



```python
response = accounts.delete(options)
```

### Tax api

Collection of different tax rates and their codes

The following arguments are required:

 * __tax_id__: The tax UUID

```python
tax = client.tax("9136fee6-02da-426d-aa01-2b50c17b8a2f")
```

##### Add (POST /core.tax/add)

Add a new tax rate

The following arguments are required:

 * __organisation_id__: The UUID of the organisation this tax rate belongs to
 * __name__: The name of this tax rate
 * __type__: The tax type (tax code)
 * __display_rate__: The rate to display this tax at
 * __effective_rate__: The rate that gets applied for this tax

```python
response = tax.add("863f2548-7284-11e3-9710-6163636f756e", "15% GST on Income", "OUTPUT2", 15, 15, options)
```

##### View (GET /core.tax/view/:tax_id)

View a tax rate



```python
response = tax.view(options)
```

##### Update (POST /core.tax/update/:tax_id)

Update an existing tax rate

The following arguments are required:

 * __organisation_id__: The UUID of the organisation this tax rate belongs to
 * __name__: The name of this tax rate
 * __type__: The tax type (tax code)
 * __display_rate__: The rate to display this tax at
 * __effective_rate__: The rate that gets applied for this tax

```python
response = tax.update("863f2548-7284-11e3-9710-6163636f756e", "15% GST on Income", "OUTPUT2", 15, 15, options)
```

### Journals api

Manages journal entries and journal lines

The following arguments are required:

 * __journal_id__: The journal entry UUID

```python
journals = client.journals("76afff0a-7368-11e3-9c55-6a6f75726e61")
```

##### Add (POST /core.journal/add)

Add a new journal entry

The following arguments are required:

 * __organisation_id__: The UUID of the organisation this journal entry belongs to
 * __journal_number__: The journal number this journal entry belongs to
 * __journal_type__: The type of journal entry this is
 * __datetime__: The timestamp this journal entry was recorded
 * __notes__: Any notes this journal entry has
 * __lines__: An array of journal lines that make up this journal entry

```python
response = journals.add("863f2548-7284-11e3-9710-6163636f756e", "200", "", "2012-09-11T00:00:00+12:00", "Common Ledger is the best!", "...", options)
```

##### View (GET /core.journal/view/:journal_id)

View a journal entry



```python
response = journals.view(options)
```

##### Add (POST /core.journal/update/:journal_id)

Add a new journal entry

The following arguments are required:

 * __organisation_id__: The UUID of the organisation this journal entry belongs to
 * __journal_number__: The journal number this journal entry belongs to
 * __journal_type__: The type of journal entry this is
 * __datetime__: The timestamp this journal entry was recorded
 * __notes__: Any notes this journal entry has
 * __lines__: An array of journal lines that make up this journal entry

```python
response = journals.update("863f2548-7284-11e3-9710-6163636f756e", "200", "", "2012-09-11T00:00:00+12:00", "Common Ledger is the best!", "...", options)
```

## Contributors
Here is a list of [Contributors]((https://github.org/commonledger/sdk-python/contributors)

### TODO

## License
MIT

## Bug Reports
Report [here](https://github.org/commonledger/sdk-python/issues).

## Contact
Patrick Hindmarsh (patrick@hindmar.sh)
