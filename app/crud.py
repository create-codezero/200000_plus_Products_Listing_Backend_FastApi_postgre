from sqlalchemy import text


def get_products(db, limit, category=None, cursor=None, snapshot=None):

    query = """
    SELECT * FROM products
    WHERE 1=1
    """

    params = {"limit": limit}

    if snapshot:
        query += " AND updated_at <= :snapshot"
        params["snapshot"] = snapshot

    if category:
        query += " AND category = :category"
        params["category"] = category

    if cursor:
        query += """
        AND (updated_at, id) < (:updated_at, :id)
        """
        params["updated_at"] = cursor["updated_at"]
        params["id"] = cursor["id"]

    query += """
    ORDER BY updated_at DESC, id DESC
    LIMIT :limit
    """

    return db.execute(text(query), params).fetchall()
