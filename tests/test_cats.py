import pytest
import datetime
import sys
sys.path.append("..")

from cdv.test import setup as setup_test
from cdv.test import block_time, CoinWrapper

from chia.util.ints import uint32, uint64
from chia.types.blockchain_format.program import Program
from chia.types.condition_opcodes import ConditionOpcode
from chia.types.spend_bundle import SpendBundle

from drivers.cat_utils import (
    SpendableCAT,
    CAT_MOD,
    construct_cat_puzzle,
    unsigned_spend_bundle_for_spendable_cats,
)


class TestFuturesLifecycle:
    @pytest.fixture(scope="function")
    async def setup(self):
        network, alice, bob = await setup_test()
        await network.farm_block()
        yield network, alice, bob

    @pytest.mark.asyncio
    async def test_lifecycle(self, setup):
        network, alice, bob = setup
        try:
            print(CAT_MOD)
            pass

        finally:
            await network.close()
