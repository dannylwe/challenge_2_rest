# challenge_2_rest

[![Build Status](https://travis-ci.org/dannylwe/challenge_2_rest.svg?branch=master)](https://travis-ci.org/dannylwe/challenge_2_rest) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9f5cb85008414e4a9a04d705af2289cd)](https://www.codacy.com/app/dannylwe/challenge_2_rest?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dannylwe/challenge_2_rest&amp;utm_campaign=Badge_Grade) [![Coverage Status](https://coveralls.io/repos/github/dannylwe/challenge_2_rest/badge.svg?branch=master)](https://coveralls.io/github/dannylwe/challenge_2_rest?branch=master) [![Maintainability](https://api.codeclimate.com/v1/badges/70b8b7e4b184c71c83b2/maintainability)](https://codeclimate.com/github/dannylwe/challenge_2_rest/maintainability)

This repo is a continuation of the branch "flask_with_tests" in the repo "andela_13".

The store manager api is hosted on Heroku at the URL "https://young-chamber-54320.herokuapp.com/". 

The api leverages flask restplus to implement [Swagger](https://swagger.io/). This assists in the API documentation and quick testing under one roof.

The API endpoints and description can be found on the index page of the app under the tab "default namesapce" and the data models used can be found under "Models".

Clicking on an individual endpoint brings a drop down of options for that endpoint, where it can be tested by utilizing the "Try it now" button.

| Method | Route | Functionality                                      |
| ---    | ---                   | ---                                |
| GET    | /hello | sanity check |
| GET    | /api/v1/attendants    | Get all attendants                 |
| DELETE | /api/v1/attendants/{id} | Get attendants by Id             |
| GET    | /api/v1/sale_order    | Get sale order                     |
| GET    | /api/v1/products      | Get all products                   |
| POST   | /api/v1/products      | Post a product                     |
| DELETE | /api/v1/products/{id} | Delete product by Id               |
| POST   | /api/v1/sale_order    | Post a sale order                  |
| POST   | /login                | Login as admin; auth by JWT cookie |
| POST   | /logout               | Logout of admin; revoke JWT        |
| POST   | /token/refresh        | Refresh JWT after expiry           |

for /login, data={"username":"admin", "password":"admin"} Content-Type; Application/JSON

