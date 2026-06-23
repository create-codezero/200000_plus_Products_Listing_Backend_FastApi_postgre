from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional

from ..db import get_db
from ..crud import get_products
from ..utils import encode_cursor, decode_cursor

router = APIRouter()


# helper: safe datetime parsing
def parse_snapshot(snapshot: Optional[str]):
    if not snapshot:
        return datetime.utcnow()

    try:
        return datetime.fromisoformat(snapshot)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid snapshot format. Use ISO format."
        )


@router.get("/products")
def list_products(
    limit: int = Query(20, ge=1, le=100),
    cursor: Optional[str] = None,
    category: Optional[str] = None,
    snapshot: Optional[str] = None,
    db: Session = Depends(get_db)
):

    # 1. snapshot handling (IMPORTANT for consistency)
    snapshot_time = parse_snapshot(snapshot)

    # 2. cursor decoding (safe)
    decoded_cursor = None
    if cursor:
        try:
            decoded_cursor = decode_cursor(cursor)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid cursor"
            )

    # 3. DB query
    rows = get_products(
        db=db,
        limit=limit,
        category=category,
        cursor=decoded_cursor,
        snapshot=snapshot_time
    )

    # 4. format response
    products = []
    next_cursor = None

    for r in rows:
        products.append({
            "public_id": r.public_id,
            "name": r.name,
            "brand": r.brand,
            "category": r.category,
            "price": r.price,
            "updated_at": r.updated_at.isoformat() if r.updated_at else None
        })

    # 5. build next cursor
    if rows:
        last = rows[-1]

        next_cursor = encode_cursor(
            last.updated_at,
            last.id
        )

    return {
        "products": products,
        "next_cursor": next_cursor,
        "snapshot": snapshot_time.isoformat()
    }