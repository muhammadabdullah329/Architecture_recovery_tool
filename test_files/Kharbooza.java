public class Kharbooza extends Melon
{
	private double antioxidants;
	public Kharbooza(int weight)
	{
		super(weight);
		antioxidants=0.00001*super.getWeight();
		super.setTotal(antioxidants);
	}
	@Override
	public double getTotal()
	{
		return super.getTotal();
	}
}