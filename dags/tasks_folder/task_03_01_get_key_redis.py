import redis

from tasks_folder import redis_conn


def run_get_key_redis():
    """
    Function to get a key from Redis
    :customer_id:
    :return:

    #>>> run_get_key_redis()
    #'145'
    """
    key_name = ''
    try:
        r = redis.Redis(host=
                        redis_conn.host
                        # 'localhost'
                        , port=6379
                        , db=1
                        , decode_responses=True)

        i = '144'
        key_name = 'Customer' + str(i)

        redis_result_get_key = r.get(key_name)

        print(type(redis_result_get_key))

        redis_result_to_dict = eval(redis_result_get_key)

        customer_id = redis_result_to_dict.get('customer_id')

        # print(customer_id)

        return 'Key ' + customer_id

    except ConnectionError:
        raise ConnectionError('Connection unsuccessful')
    except TypeError:
        print(f"Key not found: {key_name}. \n " + str(TypeError))


# run_get_key_redis()
