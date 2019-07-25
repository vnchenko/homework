create or replace PACKAGE pkg_hr AS
    PROCEDURE update_phone(
        phone_id_parameter            IN PHONE.phone_id%TYPE,
        PHONE_MODEL_parameter         IN PHONE.PHONE_MODEL%TYPE,
        PHONE_VENDOR_parameter        IN PHONE.PHONE_VENDOR%TYPE,
        PHONE_PRICE_parameter         IN PHONE.PHONE_PRICE%TYPE,
        PHONE_DATA_parameter         IN PHONE.PHONE_DATA%TYPE
        );

    FUNCTION get_phone(
        phone_id_parameter  IN PHONE.phone_id%TYPE)
    RETURN PHONE%ROWTYPE;
    END pkg_hr;


create or replace PACKAGE BODY pkg_hr AS
    PROCEDURE update_phone(
        phone_id_parameter            IN PHONE.phone_id%TYPE,
        PHONE_MODEL_parameter         IN PHONE.PHONE_MODEL%TYPE,
        PHONE_VENDOR_parameter        IN PHONE.PHONE_VENDOR%TYPE,
        PHONE_PRICE_parameter         IN PHONE.PHONE_PRICE%TYPE,
        PHONE_DATA_parameter         IN PHONE.PHONE_DATA%TYPE
        ) AS
    BEGIN
        UPDATE PHONE
        SET PHONE_MODEL = PHONE_MODEL_parameter,
            PHONE_VENDOR = PHONE_VENDOR_parameter,
            PHONE_PRICE = PHONE_PRICE_parameter,
            PHONE_DATA = PHONE_DATA_parameter
            WHERE phone_id = phone_id_parameter;
    END update_phone;

    FUNCTION get_phone(
        phone_id_parameter IN PHONE.phone_id%TYPE)
    RETURN PHONE%ROWTYPE
    AS
        phone_info PHONE%ROWTYPE;
    BEGIN
        SELECT * INTO phone_info
        FROM PHONE
        WHERE phone_id = phone_id_parameter;
    RETURN phone_info;
    END get_phone;
END pkg_hr;