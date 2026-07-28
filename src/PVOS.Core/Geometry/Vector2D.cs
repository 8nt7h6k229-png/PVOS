namespace PVOS.Core.Geometry;

public readonly record struct Vector2D(double X, double Y)
{
	public double Length => Math.Sqrt(X * X + Y * Y);

	public double LengthSquared => X * X + Y * Y;

	public Vector2D Normalize()
	{
		if (Length == 0)
			throw new InvalidOperationException("Cannot normalize a zero vector.");

		return new Vector2D(X / Length, Y / Length);
	}

	public static double Dot(Vector2D a, Vector2D b)
		=> a.X * b.X + a.Y * b.Y;

	public static Vector2D operator +(Vector2D a, Vector2D b)
		=> new(a.X + b.X, a.Y + b.Y);

	public static Vector2D operator -(Vector2D a, Vector2D b)
		=> new(a.X - b.X, a.Y - b.Y);

	public static Vector2D operator *(Vector2D v, double scalar)
		=> new(v.X * scalar, v.Y * scalar);

	public static Vector2D operator /(Vector2D v, double scalar)
	{
		if (scalar == 0)
			throw new DivideByZeroException();

		return new Vector2D(v.X / scalar, v.Y / scalar);
	}
}