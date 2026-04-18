import pandas as pd
import chess.pgn
import io


def load_data_with_clk(data_file):
    data_df = pd.read_parquet(data_file)
    data_df = data_df[["Result", "BlackElo", "WhiteElo", "Termination", "TimeControl", "moves"]]
    return data_df

def load_data_without_clk(data_file):
    data_df = pd.read_parquet(data_file)
    data_df = data_df[["Result", "BlackElo", "WhiteElo", "Termination", "TimeControl", "moves"]]

    pattern = "([a-hA-H]+[1-8]+{=[QRBN][?]|O-O|O-O-O}){2,10}"
    data_df["extracted"] = data_df["moves"].astype(str).replace(to_replace=r'(\{\[[\W.*]+\]\})', value='', regex=True)
    print(data_df.head(2))
    # data_df["moves"] = data_df["moves"].str.extractall(pattern).apply(
    #     lambda moves: 
    #         # print("moves type: ", type(moves.to_list()))
    #         # ' '.join(moves) 
    #         print("found match: ", moves.to_list(), moves[0], moves[1])
    #         # if isinstance(moves, pd.Series) and all(isinstance(move, str) for move in moves) 
    #         # else None
    #         ,
    #     axis=1
    # )
    data_df.dropna(subset=['moves'], inplace=True)
    print(data_df[["moves"]].head(2))
    return data_df


def convert_to_moves(game_moves):
    moves_stream = io.StringIO(game_moves)
    game = chess.pgn.read_game(moves_stream) # reading the game present in file
    if game is None:
        return None
    moves = []
    for node in game.mainline(): # iterating over mainline moves
        moves.append(node.move.uci())
    return moves
