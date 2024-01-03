# Integrate Khulnasoft

[![GitHub License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/khulnasoft/github-action/master/LICENSE) [![Github Action Community](https://img.shields.io/badge/community-Github%20Actions%20Discuss-343434.svg)](https://github.community/c/github-ecosystem/github-apps/64)

Securely authenticate into [Khulnasoft](https://khulnasoft.com)-generated environments to test before merge by running E2E tests against an ephemeral environment on every commit.

This action connects to Khulnasoft using your **API token** and fetches the environment variables necessary to test against your existing environments within your [GitHub Actions](https://docs.github.com/en/actions) workflow. 

## Setup
- Obtain your API token from your Khulnasoft **Org Settings** page
- Create a new GitHub repository secret named `KHULNASOFT_API_TOKEN`
- Open a PR on your Khulnasoft-enabled app

## How to use

In your GitHub workflow file located in `.github/workflows/`, you can use the **Khulnasoft GitHub Action** as per the following example:

```
on: [pull_request]

jobs:
  cypress-e2e-tests:
    runs-on: ubuntu-latest
    name: Auth into Khulnasoft and run Cypress E2E tests against ephemeral environments
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Integrate Khulnasoft
        uses: khulnasoft/khulnasoft-action@1.0.0
        env:
          KHULNASOFT_API_TOKEN: ${{ secrets.KHULNASOFT_API_TOKEN }}
      - name: Run E2E tests against the ephemeral environment
        run: npm run test
        shell: bash
        env:
            CYPRESS_BASE_URL: $KHULNASOFT_ENVIRONMENT_URL
            CYPRESS_BYPASS_TOKEN: $KHULNASOFT_BYPASS_TOKEN
        
```

This action can be configured by passing inputs or environment variables:

**Inputs**
```
  - name: Integrate Khulnasoft
    uses: khulnasoft/khulnasoft-action@1.0.0
    with:
        api-token: ${{ secrets.KHULNASOFT_API_TOKEN }}
        timeout-minutes: 30
```

| Input name | Description | Default Value |
| --------------- | --------------- |--------------- |
| `api-token` | Token required to connect to Khulnasoft's APIs. Can be obtained from your Khulnasoft **Org Settings** page | -|
| `timeout-minutes` | Number of minutes to wait for Khulnasoft environment before timing out. | 60|
| `app-name` | Filter the environments by name of the application on the Khulnasoft app. | -|


**Environment Variables**
```
  - name: Integrate Khulnasoft
    uses: khulnasoft/khulnasoft-action@1.0.0
    env:
      KHULNASOFT_API_TOKEN: ${{ secrets.KHULNASOFT_API_TOKEN }}
      KHULNASOFT_TIMEOUT: 30
      INPUT_APP_NAME: 'react-app'
```

| Environment Variable | Description | Default Value |
| --------------- | --------------- |--------------- |
| `KHULNASOFT_API_TOKEN` | Token required to connect to Khulnasoft's APIs. Can be obtained from your Khulnasoft **Org Settings** page  |-|
| `KHULNASOFT_TIMEOUT` | Number of minutes to wait for Khulnasoft environment before timing out. |60|
| `KHULNASOFT_APP_NAME` | Filter the environments by name of the application on the Khulnasoft app. |-|

**NOTE**: Inputs are given precedence over environment variables.

If input `api-token` or environment variable `KHULNASOFT_API_TOKEN` is not provided, error is raised.

On a successful run, the following environment variables are set, which can then be passed on to other actions in the same workflow:

| Parameter Name | Description |
| --------------- | --------------- |
|`KHULNASOFT_ENVIRONMENT_URL` | URL of the ephemeral environment |
|`KHULNASOFT_ENVIRONMENT_ID`  | ID of the ephemeral environment  |
|`KHULNASOFT_BYPASS_TOKEN`    | Token to bypass authentication   |


## Resources

[Khulnasoft Documentation](https://docs.khulnasoft.com/docs/)
