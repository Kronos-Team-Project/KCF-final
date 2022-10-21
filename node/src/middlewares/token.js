const jwt = require("jsonwebtoken");

const tokenMiddleware = async (req, res, next) => {
  const token =
    req.headers.authorization.split("Bearer ")[1] || req.query.token;
  if (!token) {
    res.status(401).json({
      message: "로그인 되어 있지 않음 - 1",
    });
  } else {
    try {
      jwt.verify(token, req.app.get("jwt-secret"), (err, decoded) => {
        if (err) throw new Error(err.message);
        req.decoded = decoded;
        next();
      });
    } catch (err) {
      res.status(401).json({
        message: "로그인 되어 있지 않음 - 2",
      });
    }
  }
};

module.exports = tokenMiddleware;
